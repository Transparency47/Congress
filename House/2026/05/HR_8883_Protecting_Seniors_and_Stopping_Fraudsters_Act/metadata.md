# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8883?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8883
- Title: Protecting Seniors and Stopping Fraudsters Act
- Congress: 119
- Bill type: HR
- Bill number: 8883
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-22T08:08:07Z
- Update date including text: 2026-05-22T08:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-19 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 27 - 16.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-19 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 27 - 16.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8883",
    "number": "8883",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Protecting Seniors and Stopping Fraudsters Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:07Z",
    "updateDateIncludingText": "2026-05-22T08:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 27 - 16.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
        "item": [
          {
            "date": "2026-05-21T15:06:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-19T16:04:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-19T16:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8883ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8883\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Ms. Van Duyne introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide for additional oversight of hospice programs and home health agencies under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Seniors and Stopping Fraudsters Act .\n#### 2. Revalidating enrollment of hospice programs in certain States\n##### (a) In general\nSection 1866(j) of the Social Security Act ( 42 U.S.C. 1395cc(j) ) is amended by adding at the end the following new paragraph:\n(10) Revalidation of hospice programs in certain States (A) In general In the case that the Secretary provides, pursuant to paragraph (3)(A), that new hospice programs located in a State are subject to the enhanced oversight described in such paragraph under the program under this title, the Secretary shall, not later than 1 year after the date specified in subparagraph (B) with respect to such enhanced oversight requirement, revalidate the enrollment in the program under this title of each hospice program located in such State that\u2014 (i) is not a new hospice program; and (ii) was not subject to such revalidation during the 18-month period preceding such date. (B) Date specified For purposes of subparagraph (A) , the date specified in this subparagraph is, with respect to an enhanced oversight requirement described in subparagraph (A) \u2014 (i) in the case that such requirement took effect before the date of enactment of this paragraph and is in effect on such date of enactment, such date of enactment; and (ii) in the case that such requirement takes effect on or after the date of enactment of this paragraph, such effective date. .\n##### (b) Technical correction\nSection 1866(j)(3)(A) of the Social Security Act ( 42 U.S.C. 1395cc(j)(3)(A) ) is amended by striking title XIX. and and inserting title XIX, and .\n#### 3. Additional oversight provisions for hospice programs\n##### (a) Increased survey frequency for certain hospice programs\nSection 1822(a)(1) of the Social Security Act ( 42 U.S.C. 1395i\u20136(a)(1) ) is amended\u2014\n**(1)**\nby striking Any entity and inserting:\n(A) In general Subject to subparagraph (B), any entity ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(B) Increased frequency for certain hospice programs (i) Newly enrolled; change of ownership; reactivated billing privileges Beginning 1 year after the date of enactment of this clause, a hospice program that is newly enrolled under this title, has undergone a change of ownership (as defined by the Secretary), or has reactivated billing privileges under this title in accordance with section 424.540(b) of title 42, Code of Federal Regulations (or a successor regulation), shall be subject to such a survey not less frequently than once every 12 months during the 36-month period immediately following such enrollment, change, or reactivation. (ii) Additional hospice programs (I) In general Subject to subclause (II) , beginning 1 year after the date of enactment of this clause\u2014 (aa) a hospice program that did not submit quality data to the Secretary in accordance with section 1814(i)(5)(C) for the most recent fiscal year for which data is available (as determined by the Secretary) shall be subject to such a survey not later than 18 months after the most recent such survey conducted with respect to such hospice program; and (bb) a hospice program that has a live discharge rate that is aberrant compared to peers (as determined by the Secretary) or otherwise displays characteristics or engages in practices that may indicate fraudulent or aberrant behavior (as specified by the Secretary after consultation with stakeholders, such as beneficiary advocates and representatives of the hospice industry, and the Inspector General of the Department of Health and Human Services, and updated as necessary after additional consultation with such stakeholders not less often than once every 3 years) shall be subject to such a survey not later than 18 months after the most recent such survey conducted with respect to such hospice program. (II) Limiting duplicative surveys A hospice program shall not be subject to more than 1 survey under this clause within any 18-month period. .\n##### (b) Payment adjustment if quality data not submitted\nSection 1814(i)(5) of the Social Security Act ( 42 U.S.C. 1395f(i)(5) ) is amended\u2014\n**(1)**\nin subparagraph (A)(i)\u2014\n**(A)**\nby striking for fiscal year 2024 and each subsequent fiscal year and inserting for fiscal years 2024 through 2028 ; and\n**(B)**\nby inserting , or, for fiscal year 2029 and each subsequent fiscal year, 15 percentage points after 4 percentage points ; and\n**(2)**\nin subparagraph (C), by adding at the end the following new sentence: For fiscal year 2029 and each subsequent fiscal year, in specifying a time for the submission of such data pursuant to the previous sentence, the Secretary shall establish a process under which any hospice program that has demonstrated a good faith effort to submit such data by such time may be granted additional time (not to exceed 30 days) to complete such submission. .\n#### 4. Additional oversight provisions for home health agencies\n##### (a) Increased survey frequency for certain home health agencies\nSection 1891(c)(2)(B) of the Social Security Act ( 42 U.S.C. 1395bbb(c)(2)(B) ) is amended\u2014\n**(1)**\nin clause (ii), by striking the period at the end and inserting a semicolon;\n**(2)**\nby redesignating clauses (i) and (ii) as subclauses (I) and (II), respectively, and adjusting the margins accordingly;\n**(3)**\nby striking , a standard survey and inserting the following:\n\u2014 (i) a standard survey ; and\n**(4)**\nby adding at the end the following new clauses:\n(ii) beginning 1 year after the date of enactment of this clause, in the case that the agency is newly enrolled under this title, has undergone a change of ownership (as defined by the Secretary), or has reactivated billing privileges under this title in accordance with section 424.540(b) of title 42, Code of Federal Regulations (or a successor regulation), a standard survey of an agency shall be conducted not less frequently than once every 12 months during the 36-month period immediately following such enrollment, change, or reactivation; and (iii) beginning 1 year after the date of enactment of this clause, a standard survey of an agency shall be conducted\u2014 (I) in the case that the agency did not submit quality data to the Secretary in accordance with subclauses (II) and (IV) of section 1895(b)(3)(B)(v) for the most recent year for which data is available (as determined by the Secretary), not later than 18 months after the most recent such survey conducted with respect to such agency; and (II) in the case that the agency has a beneficiary admission rate that is aberrant compared to peers (as determined by the Secretary) or otherwise displays characteristics or engages in practices that may indicate fraudulent or aberrant behavior (as specified by the Secretary after consultation with stakeholders, such as beneficiary advocates and representatives of the home health industry, and the Inspector General of the Department of Health and Human Services, and updated as necessary after additional consultation with such stakeholders not less often than once every 3 years), not later than 18 months after the most recent such survey conducted with respect to such agency, except that an agency shall not be subject to more than 1 survey under this clause within any 18-month period. .\n##### (b) Payment adjustment if quality data not submitted\nSection 1895(b)(3)(B)(v) of the Social Security Act ( 42 U.S.C. 1395fff(b)(3)(B)(v) ) is amended\u2014\n**(1)**\nin subclause (I)\u2014\n**(A)**\nby striking applicable under such clause for such year and inserting applicable under such clause for 2007 and each subsequent year through 2028 ; and\n**(B)**\nby inserting , and, for 2029 and each subsequent year, shall be reduced by 15 percentage points after 2 percentage points ;\n**(2)**\nin subclause (II), by adding at the end the following new sentence: For 2029 and each subsequent year, in specifying a time for the submission of such data pursuant to the previous sentence, the Secretary shall establish a process under which any home health agency that has demonstrated a good faith effort to submit such data by such time may be granted additional time (not to exceed 30 days) to complete such submission. ; and\n**(3)**\nin subclause (IV)(cc), by adding at the end the following new sentence: For 2029 and each subsequent year, in specifying a time for the submission of such data pursuant to the previous sentence, the Secretary shall establish a process under which any home health agency that has demonstrated a good faith effort to submit such data by such time may be granted additional time (not to exceed 30 days) to complete such submission. .\n#### 5. Enhancing enrollment screening for hospice programs and home health agencies\nSection 1866(j)(2) of the Social Security Act ( 42 U.S.C. 1395cc(j)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nin clause (i), by striking and at the end;\n**(B)**\nin clause (ii)(V), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following new clause:\n(iii) beginning 1 year after the date of enactment of this clause, in the case of a hospice program or home health agency applying for enrollment under this title that is at an extreme risk of fraud (as determined under subparagraph (G)), shall, in addition to any other screening required under this subparagraph\u2014 (I) in the case that fingerprinting is included in such screening with respect to hospice programs or home health agencies (as applicable) pursuant to clause (ii)(II), require fingerprinting of the administrator and the medical director of such hospice program or home health agency; and (II) require obtaining evidence that such hospice program or home health agency has a comprehensive liability insurance policy, as determined by the Secretary. ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(G) Hospice programs and home health agencies at extreme risk of fraud (i) In general Beginning 1 year after the date of enactment of this subparagraph, for purposes of subparagraph (B)(iii), the Secretary shall determine whether a hospice program or home health agency is at an extreme risk of fraud based on\u2014 (I) the determination made under clause (ii); and (II) such other factors as the Secretary may specify. (ii) Determination of high-risk areas For purposes of clause (i) , the Secretary shall determine whether a hospice program or home health agency is located in a State or county with respect to which, during the most recent year for which data is available, the total number of hospice programs or home health agencies (as applicable) located in such State or county significantly exceeded the total number of such programs or agencies located in such State or county during the preceding year. .\n#### 6. Additional survey and training requirements for accreditation organizations\nSection 1865 of the Social Security Act ( 42 U.S.C. 1395bb ) is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nby striking In making and inserting the following:\n(A) In making ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(B)(i) Beginning 1 year after the date of enactment of this subparagraph, the Secretary may not approve a request for a finding under paragraph (1) with respect to a national accreditation body unless the survey procedures of such accreditation body\u2014 (I) met or exceeded the standards applicable to the survey procedures that State and local agencies that have entered into an agreement with the Secretary under section 1864(a) are required to use; and (II) require surveyors to complete the relevant basic surveyor training courses offered by the Centers for Medicare & Medicaid Services before serving as a member of a survey team. (ii) The Secretary may only continue to give effect to any such finding made prior to the date that is 1 year after the date of enactment of this subparagraph with respect to a national accreditation body if the Secretary determines before such date that the survey procedures of such accreditation body meet the conditions described in clause (i) . ; and\n**(2)**\nby adding at the end the following new subsection:\n(f)(1) Not later than 1 year after the date of enactment of this subsection, the Secretary shall establish and implement a mechanism for periodically assessing the performance of an accreditation body that has received approval from the Secretary under subsection (a)(3)(A) for accreditation of provider entities. (2) In the case that the Secretary finds, pursuant to the mechanism established under paragraph (1), that the performance of such accreditation body is deficient, the Secretary shall provide for an appropriate remedy, which may include the imposition of a corrective action plan, ongoing monitoring of the accreditation body, and the termination of such approval with respect to the accreditation body for accreditation of such provider entities. .\n#### 7. Extending adjustment to calculation of hospice cap amount under Medicare\nSection 1814(i)(2)(B) of the Social Security Act ( 42 U.S.C. 1395f(i)(2)(B) is amended\u2014\n**(1)**\nin clause (ii), by striking 2035 and inserting 2036 ; and\n**(2)**\nin clause (iii), by striking 2035 and inserting 2036 .\n#### 8. Requiring notice regarding revocation of hospice program election under Medicare\n##### (a) In general\nSection 1812(d)(2) of the Social Security Act ( 42 U.S.C. 1395d(d)(2) ) is amended by adding at the end the following new subparagraph:\n(E) With respect to elections under this paragraph made on or after the date that is 1 year after the date of enactment of this subparagraph, the Secretary shall, not later than 15 calendar days after the effective date of such election, provide to such individual written notice of such election. Such notice shall display the toll-free telephone number 1\u2013800\u2013MEDICARE, and shall include\u2014 (i) the name, address, and telephone number of the hospice program with respect to which such election is made; (ii) a description, in plain language, of the waiver of rights applicable under subparagraph (A); and (iii) an explanation of how such individual may revoke such election under subparagraph (B) or change the hospice program with respect to which such election is made under subparagraph (C). .\n##### (b) Funding\nSection 1812 of the Social Security Act ( 42 U.S.C. 1395d ) is amended by adding at the end the following new subsection:\n(h) Funding for election notices The Secretary shall provide for the transfer, from the Federal Hospital Insurance Trust Fund under section 1817 to the Centers for Medicare & Medicaid Services Program Management Account, of $6,000,000 for each fiscal year (beginning with fiscal year 2026) for purposes of carrying out subsection (d)(2)(E). Sums so transferred shall remain available until expended. .\n#### 9. Report on program integrity activities\n##### (a) In general\nNot later than the date that is 1 year after the date of the enactment of this section, and annually thereafter for a period of 5 years, the Secretary of Health and Human Services shall report to the appropriate committees of Congress on the outcome of program integrity activities conducted with respect to hospice programs or home health agencies enrolled under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), which shall include the following information with respect to the preceding year:\n**(1)**\nA description of each type of entity of the Centers for Medicare & Medicaid Services that conducted reviews, audits, or any other program integrity activities with respect to hospice programs or home health agencies enrolled under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).\n**(2)**\nThe number of reviews, audits, or other program integrity activities performed by each such type of entity with respect to hospice programs or home health agencies.\n**(3)**\nA description of any trends, including instances of individual physicians with high rates of ineligible certifications, identified by such entities with respect to improper payments made to hospice programs or home health agencies.\n**(4)**\nAny findings made by such entities with respect to reviews, audits, or other program integrity activities conducted with respect to hospice programs and home health agencies.\n**(5)**\nThe number and nature of enforcement actions taken by the Centers for Medicare & Medicaid Services with respect to hospice programs and home health agencies as a result of the findings described in paragraph (4) , including the number of revocations of enrollment in the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) of hospice programs and home health agencies.\n**(6)**\nA description of any actions taken by the Centers for Medicare & Medicaid Services to reduce duplication of efforts among such entities, including any actions taken to prevent or mitigate the administrative burden on hospice programs and home health agencies associated with program integrity activities.\n##### (b) Definitions\nIn this section:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Ways and Means and the Committee on Energy and Commerce of the House of Representatives; and\n**(B)**\nthe Committee on Finance of the Senate.\n**(2) Home health agency**\nThe term home health agency has the meaning given such term in section 1861(o) of the Social Security Act ( 42 U.S.C. 1395x(o) ).\n**(3) Hospice program**\nThe term hospice program has the meaning given such term in section 1861(dd)(2) of the Social Security Act ( 42 U.S.C. 1395x(dd)(2) ).\n#### 10. Funding\nThe Secretary of Health and Human Services shall provide for the transfer from the Federal Hospital Insurance Trust Fund established under section 1817 of the Social Security Act ( 42 U.S.C. 1395i ) to the Centers for Medicare & Medicaid Services\u2019 Program Management Account of $100,000,000 for fiscal year 2026 for purposes of carrying out section 1822(a)(1) of such Act, as amended by section section 3(a) , and section 1891(c)(2) of such Act, as amended by section section 4(a) . Sums so transferred shall remain available until expended. Any transfer pursuant to this subsection shall be in addition to any transfer pursuant to section 3(a)(2) of the Improving Medicare Post-Acute Care Transformation Act of 2014.",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8883ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Protecting Seniors and Stopping Fraudsters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T14:38:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Seniors and Stopping Fraudsters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T14:38:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide for additional oversight of hospice programs and home health agencies under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T14:33:33Z"
    }
  ]
}
```
