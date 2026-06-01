# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4470
- Title: Removing Burdens From Organ Donation Act
- Congress: 119
- Bill type: HR
- Bill number: 4470
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2025-09-11T17:22:28Z
- Update date including text: 2025-09-11T17:22:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-16 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-16 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4470",
    "number": "4470",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
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
    "title": "Removing Burdens From Organ Donation Act",
    "type": "HR",
    "updateDate": "2025-09-11T17:22:28Z",
    "updateDateIncludingText": "2025-09-11T17:22:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-16T14:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "WA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "WV"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "HI"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "IL"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "MO"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4470ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4470\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Ms. Van Duyne (for herself, Ms. DelBene , Mrs. Miller of West Virginia , and Mr. Costa ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XI of the Social Security Act to require hospitals participating in the Medicare and Medicaid programs to establish certain notification procedures with respect to organ procurement agencies.\n#### 1. Short title\nThis Act may be cited as the Removing Burdens From Organ Donation Act .\n#### 2. Notifying organ procurement agencies with respect to potential organ donors\n##### (a) In general\nSection 1138(a) of the Social Security Act ( 42 U.S.C. 1320b\u20138(a) ) is amended\u2014\n**(1)**\nin paragraph (1)(A)(iii)\u2014\n**(A)**\nby adding and at the end;\n**(B)**\nby striking that such and inserting\nthat\u2014 (I) such ; and\n**(C)**\nby adding at the end the following new subclause:\n(II) subject to paragraph (4), beginning on the date that is 2 years after the date of the enactment of the Removing Burdens From Organ Donation Act, with respect to such a potential organ donor, such hospital\u2019s designated organ procurement agency is issued an automated electronic notification and is provided electronic and remote access to the electronic health records of such potential organ donor when such electronic health records are updated to indicate that such potential organ donor is deceased or that the death of such potential organ donor is imminent, as determined in accordance with the protocol described in section 482.45(a)(1) of title 42, Code of Federal Regulations (or any successor regulation); ; and\n**(2)**\nby adding at the end the following new paragraph:\n(4) Exemptions from automated EHR access requirement (A) Exemptions (i) In general The Secretary may exempt a hospital or critical access hospital from the automated electronic notification and remote access requirement under paragraph (1)(A)(iii)(II) for a period of 3 years if the Secretary determines that meeting such requirement would result in a significant hardship, such as in the case of a hospital or critical access hospital located in a rural area without sufficient Internet access, or other exceptional circumstances demonstrated by the hospital. (ii) Automatic exemption The Secretary shall grant an exemption described in clause (i) to a hospital or critical access hospital for a period of 1 year if the Secretary determines that such hospital is affected by a cybersecurity attack (as defined in subparagraph (C) ), or is located in an area affected by a major disaster (as defined in section 5122(2) of title 42, United States Code) or any other natural or man-made disaster, and shall notify such hospital or critical access hospital of such exemption. (iii) Extension The Secretary may extend an exemption granted under clause (i) or (ii) if the hospital or critical access hospital demonstrates to the satisfaction of the Secretary that such an extension is necessary. (B) Report Not later than 2 years after the date of the enactment of the Removing Burdens From Organ Donation Act, and not less frequently than annually thereafter, the Secretary shall submit to the Committee on Ways and Means and the Committee on Energy and Commerce of the House of Representatives, and to the Committee on Finance and the Committee on Health, Education, Labor, and Pensions of the Senate, a report on the number of exemptions granted under subparagraph (A) during the previous year and the reason for granting each such exemption. (C) Cybersecurity attack defined For purposes of subparagraph (A) , the term cybersecurity attack means, with respect to a hospital or a critical access hospital, any kind of malicious activity that\u2014 (i) attempts to collect, modify, disrupt, deny, degrade, or destroy information system resources of the hospital, including the information itself; (ii) affects the confidentiality, integrity or availability of data, information, or operational technology system resources of the hospital; or (iii) poses any other threat to the information, information systems, technology, or technological capabilities of the hospital, as determined by the Secretary. .\n##### (b) Guidance on best practices\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall issue guidance to hospitals, critical access hospitals, organ procurement agencies, and electronic health record companies regarding best practices for complying with the automated electronic notification and remote access requirement under subclause (II) of section 1138(a)(1)(A)(iii) of the Social Security Act ( 42 U.S.C. 1320b\u20138(a)(1)(A)(iii) ), as added by subsection (a). Such guidance shall be based upon the experiences of entities that have previous experience with the implementation of similar automated electronic notifications and remote access, and shall provide insights on what worked well and what did not.\n**(2) Explanation of changes to donors and family members**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall issue guidance to State health agencies (or such other State agency, department, or authority as the Governor of each State may determine appropriate) regarding best practices for explaining the automated electronic notification and remote access requirement under subclause (II) of section 1138(a)(1)(A)(iii) of the Social Security Act ( 42 U.S.C. 1320b\u20138(a)(1)(A)(iii) ), as added by subsection (a), to organ donors, potential organ donors, and the family members of such donors and potential donors.\n##### (c) GAO report and study\nThe Comptroller General of the United States (in this subsection referred to as the Comptroller General ) shall\u2014\n**(1)**\ncarry out a study on the implementation of the automated electronic notification and remote access requirement under subclause (II) of section 1138(a)(1)(A)(iii) of the Social Security Act ( 42 U.S.C. 1320b\u20138(a)(1)(A)(iii) ), as added by subsection (a), that takes into account\u2014\n**(A)**\nthe cost of implementing the automated electronic notification and remote access requirement described in such paragraph;\n**(B)**\nthe impact of hospital location on the implementation of such requirement, including the impact of limited broadband access in rural areas, and improvements that could be made to facilitate such implementation; and\n**(C)**\nthe reports submitted by the Secretary pursuant to paragraph (4)(B) of section 1138(a) of such Act ( 42 U.S.C. 1320b\u20138(a) ), as added by subsection (a); and\n**(2)**\nnot later than 3 years after the date of the enactment of the Removing Burdens from Organ Donation Act, submit to Congress a report on the results of the study carried out under paragraph (1) that includes\u2014\n**(A)**\nan analysis of data maintained by the Department of Health and Human Services related to the outcomes of organ transplants performed after the enactment of the Removing Burdens from Organ Donation Act;\n**(B)**\na review of issues related to securing patient data and the roles of the Centers for Medicare & Medicaid Services and the Health Resources and Services Administration with respect to those issues; and\n**(C)**\nany recommendations for further action, as appropriate.",
      "versionDate": "2025-07-16",
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
        "name": "Health",
        "updateDate": "2025-09-11T17:22:28Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4470ih.xml"
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
      "title": "Removing Burdens From Organ Donation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Removing Burdens From Organ Donation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XI of the Social Security Act to require hospitals participating in the Medicare and Medicaid programs to establish certain notification procedures with respect to organ procurement agencies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T05:48:16Z"
    }
  ]
}
```
