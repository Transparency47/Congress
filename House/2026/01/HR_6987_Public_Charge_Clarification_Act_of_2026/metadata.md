# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6987?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6987
- Title: Public Charge Clarification Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6987
- Origin chamber: House
- Introduced date: 2026-01-08
- Update date: 2026-02-13T09:06:52Z
- Update date including text: 2026-02-13T09:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-08: Introduced in House

## Actions

- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6987",
    "number": "6987",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Public Charge Clarification Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-13T09:06:52Z",
    "updateDateIncludingText": "2026-02-13T09:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-08",
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
        "item": {
          "date": "2026-01-08T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "AL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "WI"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "AZ"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NC"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "SC"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6987ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6987\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 8, 2026 Mr. Nehls (for himself, Mr. Moore of Alabama , Mr. Weber of Texas , Mr. Grothman , Mr. Roy , Mr. Gosar , Mr. Harris of North Carolina , Mr. Hunt , Mr. Jackson of Texas , and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to clarify the definition of public charge and likely at any time to become a public charge, to establish requirements for affidavits of support and public charge bonds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Charge Clarification Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSection 212(a)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(4) ) establishes that an alien who, in the opinion of the consular officer or the Attorney General, is likely at any time to become a public charge is inadmissible.\n**(2)**\nCongress has laid out specific factors to be considered in determining whether an alien is likely to become a public charge, including the alien\u2019s age, health, family status, assets, resources, financial status, education, and skills, as well as any affidavit of support under section 213A.\n**(3)**\nThese statutory factors have not been faithfully applied in the intended totality of the circumstances analysis by executive agencies, leading to inconsistent and overly permissive interpretations that undermine congressional intent to ensure self-sufficiency among immigrants.\n**(4)**\nThe proposed rule entitled Inadmissibility on Public Charge Grounds, published by the Department of Homeland Security in the Federal Register on October 10, 2018 (83 FR 51114), provided a clear framework for identifying public benefits that render an alien a public charge, including both monetizable and non-monetizable benefits.\n**(5)**\nTo protect American taxpayers and promote immigrant self-sufficiency, it is necessary to codify and expand upon this framework, ensuring that all current and future government benefits are considered in public charge determinations.\n#### 3. Definition of public charge\nSection 212(a)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(4) ) is amended to read as follows:\n(4) Public charge (A) In general Any alien who, in the opinion of the consular officer at the time of application for a visa, or in the opinion of the Attorney General at the time of application for admission or adjustment of status, is likely at any time to become a public charge is inadmissible. (B) Definition For purposes of this paragraph\u2014 (i) The term public charge means an alien who receives one or more public benefits (as defined in subparagraph (C)) for more than 12 months in the aggregate within any 36-month period (such that, for instance, receipt of two benefits in one month counts as two months). (ii) An alien is likely at any time to become a public charge if the alien is likely to receive one or more public benefits (as defined in subparagraph (C)) for more than 12 months in the aggregate within any 36-month period after the date of admission or adjustment of status. (C) Public benefits defined The term public benefits means any Federal, State, local, or tribal cash assistance for income maintenance, supplemental nutrition assistance, housing assistance, non-emergency medical assistance, or other similar benefits, including all monetizable and non-monetizable benefits as defined in the proposed rule entitled Inadmissibility on Public Charge Grounds, published in the Federal Register on October 10, 2018 (83 FR 51114). This definition shall include\u2014 (i) Supplemental Security Income (SSI) under title XVI of the Social Security Act; (ii) Temporary Assistance for Needy Families (TANF) under part A of title IV of the Social Security Act; (iii) Any Federal, State, local, or tribal cash benefit program for income maintenance; (iv) The Supplemental Nutrition Assistance Program (SNAP) under the Food and Nutrition Act of 2008; (v) Section 8 Housing Choice Voucher Program under section 8 of the United States Housing Act of 1937; (vi) Section 8 Project-Based Rental Assistance (including Moderate Rehabilitation) under section 8 of the United States Housing Act of 1937; (vii) Public housing under section 9 of the United States Housing Act of 1937; (viii) Medicaid under title XIX of the Social Security Act (except for emergency medical assistance, benefits provided to individuals under 21 years of age, or benefits provided to pregnant women); (ix) Premium and cost-sharing subsidies under section 36B of the Internal Revenue Code of 1986 (relating to refundable credit for coverage under a qualified health plan) or section 1402 of the Patient Protection and Affordable Care Act (relating to reduced cost sharing); and (x) Any other Federal, State, local, or tribal program providing monetizable or non-monetizable benefits, including programs created after the date of enactment of the Public Charge Clarification Act of 2025. (D) Publication of list of benefits Not later than 180 days after the date of enactment of the Public Charge Clarification Act of 2025, the Secretary of Homeland Security, acting through the Director of U.S. Citizenship and Immigration Services, shall publish in the Federal Register a comprehensive list of all public benefits (as defined in subparagraph (C)) that may render an alien a public charge or likely to become a public charge. The Secretary shall update such list as necessary to include any new programs or benefits created after publication and shall publish notice of such updates in the Federal Register. (E) Factors to be considered In determining whether an alien is inadmissible under this paragraph, the consular officer or the Attorney General shall consider, in the totality of the circumstances, the alien\u2019s\u2014 (i) age; (ii) health; (iii) family status; (iv) assets, resources, and financial status; (v) education and skills; (vi) prospective immigration status and expected period of admission; and (vii) any affidavit of support under section 213A. No single factor shall be dispositive, and the determination shall be based on a holistic assessment of the alien\u2019s likelihood of becoming a public charge. (F) Exemptions This paragraph shall not apply to\u2014 (i) refugees admitted under section 207; (ii) asylees granted asylum under section 208; or (iii) aliens serving in the Armed Forces of the United States or the dependents of such aliens. (G) Waivers No waiver of inadmissibility under this paragraph shall be granted to any alien not exempted under subparagraph (F), unless specifically authorized by an Act of Congress. (H) Affidavits of support (i) An affidavit of support under section 213A may be considered as one factor in the totality of the circumstances under subparagraph (E), but shall not be sufficient, standing alone, to overcome a finding that an alien is likely to become a public charge. (ii) Any affidavit of support submitted under section 213A shall be accompanied by documentary evidence demonstrating the sponsor\u2019s ability to financially support the alien and all members of the sponsor\u2019s household, including proof of income, assets, and resources sufficient to maintain the household at an annual income equal to at least 125 percent of the Federal poverty line. (I) Public charge bonds (i) The consular officer or the Attorney General shall require the posting of a public charge bond as a condition of admission or adjustment of status if the alien is determined to be likely to become a public charge but other factors warrant conditional approval. (ii) Such bond shall be in an amount of not less than $10,000, payable to the United States, and shall be forfeited if the alien becomes a public charge within 10 years of admission or adjustment of status. (iii) The Secretary of Homeland Security shall establish regulations for the administration, forfeiture, and cancellation of such bonds. .\n#### 4. Conforming amendments\n##### (a)\nSection 213A of the Immigration and Nationality Act ( 8 U.S.C. 1183a ) is amended by adding at the end the following:\n(i) Requirements for public charge determinations Affidavits of support under this section shall comply with the requirements of section 212(a)(4)(H). .\n##### (b)\nAny reference in Federal law or regulation to public charge or likely to become a public charge shall be construed in accordance with the amendments made by this Act.\n#### 5. Effective date\nThe amendments made by this Act shall take effect 180 days after the date of enactment of this Act and shall apply to all applications for visas, admission, or adjustment of status pending on or filed after such effective date.",
      "versionDate": "2026-01-08",
      "versionType": "Introduced in House"
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
        "name": "Immigration",
        "updateDate": "2026-01-26T13:42:25Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6987ih.xml"
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
      "title": "Public Charge Clarification Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Charge Clarification Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to clarify the definition of \"public charge\" and \"likely at any time to become a public charge,\" to establish requirements for affidavits of support and public charge bonds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T03:33:18Z"
    }
  ]
}
```
