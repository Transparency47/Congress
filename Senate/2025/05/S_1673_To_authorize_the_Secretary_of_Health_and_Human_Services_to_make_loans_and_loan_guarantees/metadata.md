# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1673?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1673
- Title: Mental Health Infrastructure Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1673
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-12-10T07:02:18Z
- Update date including text: 2025-12-10T07:02:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1673",
    "number": "1673",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Mental Health Infrastructure Improvement Act of 2025",
    "type": "S",
    "updateDate": "2025-12-10T07:02:18Z",
    "updateDateIncludingText": "2025-12-10T07:02:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-05-08T16:27:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MS"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1673is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1673\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Merkley (for himself and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo authorize the Secretary of Health and Human Services to make loans and loan guarantees for planning, constructing, or renovating pediatric or adult mental health treatment facilities and pediatric or adult substance use disorder treatment facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mental Health Infrastructure Improvement Act of 2025 .\n#### 2. Loans and loan guarantees\nPart P of title III of the Public Health Service Act is amended by inserting after section 399V\u20137 of such Act ( 42 U.S.C. 280g\u201318 ) the following:\n399V\u20138. Loans and loan guarantees for planning, constructing, or renovating eligible facilities for pediatric or adult mental health and substance use disorder services (a) In general The Secretary may\u2014 (1) make loans and loan guarantees to eligible entities for the purpose of\u2014 (A) constructing or renovating, including planning the construction or renovation of, a pediatric or adult mental health treatment facility or a pediatric or adult substance use disorder treatment facility; (B) improving digital infrastructure, telehealth capabilities, or other patient care infrastructure at such a facility; or (C) adding, or converting beds to, adult or pediatric psychiatric and substance use inpatient beds at such a facility; and (2) subject to subsection (e), make loans and loan guarantees for refinancing loans that were made for such purpose to an eligible entity. (b) Preference In making loans and loan guarantees under this section, the Secretary shall give preference to eligible entities proposing to construct or renovate a pediatric or adult mental health treatment facility, or a pediatric or adult substance use disorder treatment facility, as determined by the Secretary, that will\u2014 (1) increase the number of pediatric or adult psychiatric beds or pediatric or adult substance use disorder beds in a county that has insufficient psychiatric or substance use disorder treatment bed capacity; (2) provide mental health or substance use disorder services in a high-need rural or underresourced community; (3) provide multiple services across the continuum of mental health or substance use disorder care; or (4) have the capacity to provide integrated or specialized mental health and substance use disorder care for complex cases or patients with medical co-morbidities. (c) Set-Aside The Secretary shall allocate at least 25 percent of the funds under this section for any fiscal year for awards to construct or renovate facilities serving primarily pediatric and adolescent populations. (d) Terms and conditions Loans and loan guarantees under this section shall be made on such terms and conditions as the Secretary may prescribe, subject to the provisions of this section including the following: (1) The Secretary may allow credit to a prospective borrower only where\u2014 (A) it is necessary to increase the number of psychiatric or substance use disorder treatment facilities to enhance the public\u2019s access to a comprehensive continuum of mental health and substance use disorder services; and (B) a credit subsidy is the most efficient way to achieve such increase (on a borrower-by-borrower basis). (2) The final maturity of loans made or guaranteed under this section shall not exceed a period of 20 years, or the period of 50 percent of the useful life of any physical asset to be financed by the loan, whichever is less as determined by the Secretary. (3) The Secretary may not make a loan guarantee under this section, with respect to any borrower, in excess of 80 percent of any potential loss on the loan. (4) The Secretary may not make any loan or loan guarantee under this section if the loan will be subordinated\u2014 (A) to another debt contracted by the borrower; or (B) to any other claims against the borrower in the case of default. (5) The Secretary may not make any loan guarantee under this section unless the Secretary determines, at the Secretary\u2019s discretion, that\u2014 (A) the lender is responsible; and (B) adequate provision is made for servicing the loan on reasonable terms and protecting the financial interest of the United States. (6) The Secretary may not make any loan guarantee under this section if the income from the loan will be excluded from gross income for purposes of chapter 1 of the Internal Revenue Code of 1986. (7) The Secretary may not make any loan or loan guarantee under this section unless\u2014 (A) the loan and interest supplements on any loan guarantee will be at an interest rate that is set by reference to a benchmark interest rate on marketable Treasury securities with a similar maturity to the loan being made or guaranteed; and (B) the minimum interest rate on the loan\u2014 (i) will be no less than the estimated cost to the Government of making the loan plus 1 percent, with the goal of keeping the interest rate below the interest rate of a comparable and competitive private sector benchmark financial instrument; and (ii) will be adjusted, as determined by the Secretary, every quarter to take account of changes in the interest rate of the benchmark financial instrument. (8) The Secretary may not make any loan or loan guarantee under this section unless\u2014 (A) fees or premiums on the loan or loan guarantee and corresponding insurance coverage will be set at levels that minimize the cost to the Government (as defined in section 502(5) of the Federal Credit Reform Act of 1990) of insuring such loan or loan guarantee, while supporting achievement of enhancing the public\u2019s access to a comprehensive continuum of mental health and substance use disorder services, including increasing the number of inpatient psychiatric and substance use disorder bed counts in areas with insufficient bed capacity; (B) the minimum guarantee fee or insurance premium imposed by the Government will be no less than the level sufficient to cover all of the estimated costs to the Government of the expected default claims, plus one percent; and (C) loan guarantee fees imposed by the Government will be reviewed every six months to ensure that the fees imposed on new loan guarantees are at a level sufficient to satisfy subparagraph (B) based on the most recent estimates of such costs. (9) The provisions of any loan guarantee under this section shall state that the guarantee is conclusive evidence that\u2014 (A) the guarantee has been properly obtained; (B) the underlying loan qualified for the guarantee; and (C) except in the case of fraud or material misrepresentation by the holder of the loan, the guarantee will be presumed to be valid, legal, and enforceable. (10) The Secretary may not make any loan or loan guarantee under this section unless\u2014 (A) the borrower finances at least 25 percent of the funded project from other sources; and (B) the borrower uses funds that were not derived from Federal loans or loan guarantees to pay the fees or premiums on the loan or loan guarantee under this section. (11) The Secretary\u2014 (A) shall prescribe explicit standards for use in periodically assessing the credit risk of new and existing direct loans and guaranteed loans; and (B) shall not make a loan or loan guarantee under this section unless the Secretary finds that there is a reasonable assurance of repayment. (e) Limitation on refinancing The authority vested by subsection (a)(2)\u2014 (1) authorizes making loans and loan guarantees only for refinancing loans that are entered into on or before the date that is 24 months before the date of enactment of the Mental Health Infrastructure Improvement Act of 2025 ; and (2) terminates on the date that is 24 months after such date of enactment. (f) Payment of losses (1) Default on guaranteed loans If, as a result of a default by a borrower under a loan guaranteed under this section, after the holder thereof has made such further collection efforts and instituted such enforcement proceedings as the Secretary may require, the Secretary determines that the holder has suffered a loss\u2014 (A) the Secretary shall pay to such holder 75 percent of such loss, as specified in the guarantee contract; (B) upon making any such payment, the Secretary shall be subrogated to all the rights of the recipient of the payment; and (C) the Secretary shall be entitled to recover from the borrower the amount of any payments made pursuant to the guarantee contract. (2) Required enforcement of Federal rights The Attorney General of the United States shall take such action as may be appropriate to enforce any right accruing to the United States as a result of the issuance of any guarantee under this section. (3) Forbearance Nothing in this section precludes any forbearance for the benefit of the borrower of a loan that is made or guaranteed under this section which is agreed upon by the parties to the loan and approved by the Secretary, provided that budget authority for any resulting cost to the Government (as defined in section 502(5) of the Federal Credit Reform Act of 1990) is available. (g) Definitions In this section: (1) The term children\u2019s hospital means a hospital that predominantly serves patients under the age of 18. (2) The term critical access hospital has the meaning given to such term in section 1861(mm) of the Social Security Act. (3) The term eligible entity means public, private for-profit, and private not-for-profit\u2014 (A) hospitals including general acute hospitals, psychiatric hospitals, critical access hospitals, rural emergency hospitals, sole community hospitals, children\u2019s hospitals, and other hospitals as specified by the Secretary; (B) substance use disorder treatment facilities; (C) mental health treatment facilities; (D) facilities that employ licensed mental health and substance use disorder professionals, such as child, adolescent, and adult psychiatrists, child, adolescent, and adult psychologists, advanced practice registered nurses, social workers, licensed professional counselors, or other licensed professionals that provide mental health or substance use disorder services to pediatric, adolescent, or adult patients; (E) alliances of hospitals or facilities listed in any of subparagraphs (A) through (D); and (F) other facilities as determined by the Secretary. (4) The term mental health treatment facility \u2014 (A) includes\u2014 (i) a child, adolescent, or adult outpatient facility that provides\u2014 (I) intensive outpatient services; (II) partial hospitalization services; (III) crisis intervention and stabilization; or (IV) other mental, behavioral, or emotional health services deemed appropriate by the Secretary; (ii) a hospital (including a general acute hospital, a psychiatric hospital, a critical access hospital, a rural emergency hospital, a sole community hospital, a children\u2019s hospital, or other type of hospital as specified by the Secretary) that\u2014 (I) provides acute, short-term inpatient psychiatric treatment services or outpatient services; and (II) may include a military services program to meet the needs of active and retired military servicemembers; and (iii) a facility within or near an emergency department for providing discharge planning and instructions to emergency department patients in need of mental health or substance use disorder treatment and transfer to an appropriate mental health or substance use disorder treatment care setting; and (B) excludes a facility that provides long-term inpatient care. (5) The term psychiatric hospital has the meaning given to such term in section 1861(f) of the Social Security Act. (6) The term rural emergency hospital has the meaning given to such term in section 1861(kkk) of the Social Security Act. (7) The term sole community hospital has the meaning given to such term in section 1886(d)(5)(D)(iii) of the Social Security Act. (8) The term substance use disorder treatment facility \u2014 (A) includes\u2014 (i) a child, adolescent, or adult outpatient facility that provides outpatient substance use disorder services; and (ii) a hospital (including a general acute hospital, a psychiatric hospital, a critical access hospital, a rural emergency hospital, a sole community hospital, a children\u2019s hospital, or other type of hospital as specified by the Secretary) that\u2014 (I) provides acute, short-term inpatient substance use disorder treatment services or outpatient services; and (II) may include a military services program to meet the needs of active and retired military servicemembers; and (B) excludes any facility described in paragraph (4)(B). (h) Funding limitations The Secretary may provide loans and loan guarantees under this section\u2014 (1) only to the extent or in the amounts provided in advance in appropriation Acts; and (2) totaling not more than $200,000,000 for each of fiscal years 2026 through 2030. .\n#### 3. Mental Health and Substance Use Treatment Trust Fund\n##### (a) Establishment\nThere is established in the Treasury of the United States a trust fund to be known as the Mental Health and Substance Use Treatment Trust Fund (in this section referred to as the Trust Fund ).\n##### (b) Deposits\nThere are hereby authorized to be appropriated to the Trust Fund, to remain available until expended, amounts equivalent to any revenues from the program of loans and loan guarantees under section 399V\u20138 of the Public Health Service Act, as added by section 2, that exceed the costs of carrying out such program.\n##### (c) Use of fund\nAmounts in the Trust Fund shall be available, as provided by appropriation Acts, for block grants for community mental health services under subpart I of part B of title XIX of the Public Health Service Act ( 42 U.S.C. 300x et seq. ).",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-18",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2223",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Building Capacity for Care Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-08",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3266",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Mental Health Infrastructure Improvement Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-06-03T13:06:07Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1673is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Mental Health Infrastructure Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mental Health Infrastructure Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of Health and Human Services to make loans and loan guarantees for planning, constructing, or renovating pediatric or adult mental health treatment facilities and pediatric or adult substance use disorder treatment facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:33:27Z"
    }
  ]
}
```
