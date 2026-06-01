# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7759?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7759
- Title: Afghanistan Vetting and Accountability Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7759
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-03-19T15:29:33Z
- Update date including text: 2026-03-19T15:29:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7759",
    "number": "7759",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Afghanistan Vetting and Accountability Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-19T15:29:33Z",
    "updateDateIncludingText": "2026-03-19T15:29:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:00:35Z",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "AZ"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7759ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7759\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Barr (for himself, Mr. Biggs of Arizona , and Mr. Pfluger ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require verification of the personal and biometric information of all individuals evacuated from Afghanistan, to require in-person interviews of such individuals, and to prohibit Afghan evacuees who do not provide such information or submit to such interviews from receiving Federal assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Afghanistan Vetting and Accountability Act of 2026 .\n#### 2. Verification and vetting requirements with respect to individuals evacuated from Afghanistan\n##### (a) Definitions\nIn this section:\n**(1) Federal means-tested public benefit**\nThe term Federal means-tested public benefit means a Federal means-tested public benefit within the meaning of section 403 of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1613 ).\n**(2) Individual evacuated from Afghanistan**\nThe term individual evacuated from Afghanistan \u2014\n**(A)**\nmeans any individual, other than a United States citizen or a member of the United States Armed Forces, conveyed out of Afghanistan into the United States in coordination with the Government of the United States during the period beginning on January 20, 2021, and ending on January 20, 2022; and\n**(B)**\nincludes each individual, other than a United States citizen or a member of the United States Armed Forces, evacuated from Afghanistan as part of Operation Allies Welcome.\n**(3) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n**(4) Unemployment compensation**\nThe term unemployment compensation has the meaning given the term in section 85(b) of the Internal Revenue Code of 1986.\n##### (b) Verification and vetting requirements\n**(1) In general**\nThe Secretary shall verify the personal and biometric information and conduct in-person vetting of each individual evacuated from Afghanistan.\n**(2) Vetting database**\nThe Secretary shall develop and maintain a database that contains, for each individual evacuated from Afghanistan, the following:\n**(A)**\nPersonal information, including name and date of birth.\n**(B)**\nBiometric information.\n**(C)**\nAny criminal record since the date on which the individual entered the United States.\n**(D)**\nAny application for, or receipt of, unemployment compensation or a Federal means-tested public benefit.\n**(E)**\nThe vetting status of the individual, including whether the individual has undergone in-person vetting.\n##### (c) Quarterly report\n**(1) In general**\nNot less frequently than quarterly until the date on which the Secretary submits the certification under subsection (d), the Secretary shall submit to Congress a report detailing the compliance of the Secretary with subsection (b).\n**(2) Elements**\nEach report required by paragraph (1) shall include the following:\n**(A)**\nA list of all individuals evacuated from Afghanistan.\n**(B)**\nWith respect to each such individual\u2014\n**(i)**\nvetting status, including whether the individual has undergone in-person vetting;\n**(ii)**\nan assessment as to whether the individual has received unemployment compensation or a Federal means-tested benefit;\n**(iii)**\na description of any arrest or criminal record for conduct that occurred in Afghanistan, if available; and\n**(iv)**\na description of any arrest or criminal record for conduct that occurred in the United States.\n**(C)**\nThe estimated number of days remaining until the Secretary completes the verification and vetting of each individual evacuated from Afghanistan as required by subsection (b)(1).\n##### (d) Certification\nNot later than 30 days after the date on which the Secretary completes the verification and vetting required by subsection (b)(1), the Secretary shall submit to Congress a certification that such verification and vetting has been completed.\n##### (e) GAO Audits and Reports\n**(1) Audits**\nThe Comptroller General of the United States shall conduct an audit and investigation with respect to the compliance of the Secretary with this Act\u2014\n**(A)**\nnot later than 2 years after the date of the enactment of this Act; and\n**(B)**\nnot later than 1 year after the date on which the Secretary makes the certification under subsection (d).\n**(2) Reports**\nNot later than 30 days after the completion of each audit and investigation required by paragraph (1), the Comptroller General shall submit to Congress a report on the results of the audit and investigation.\n##### (f) Restriction on Federal assistance\nAn individual evacuated from Afghanistan who has not provided personal information and biometric information to the Secretary, and undergone in-person vetting, shall not be eligible to receive unemployment compensation or any Federal means-tested public benefit.",
      "versionDate": "2026-03-03",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-12-02",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3310",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Afghanistan Vetting and Accountability Act of 2025",
      "type": "S"
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
        "updateDate": "2026-03-19T15:29:33Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7759ih.xml"
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
      "title": "Afghanistan Vetting and Accountability Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T08:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Afghanistan Vetting and Accountability Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T08:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require verification of the personal and biometric information of all individuals evacuated from Afghanistan, to require in-person interviews of such individuals, and to prohibit Afghan evacuees who do not provide such information or submit to such interviews from receiving Federal assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T08:03:26Z"
    }
  ]
}
```
