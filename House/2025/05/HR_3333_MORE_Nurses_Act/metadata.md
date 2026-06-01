# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3333
- Title: MORE Nurses Act
- Congress: 119
- Bill type: HR
- Bill number: 3333
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2026-01-21T09:05:41Z
- Update date including text: 2026-01-21T09:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3333",
    "number": "3333",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "MORE Nurses Act",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:41Z",
    "updateDateIncludingText": "2026-01-21T09:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:03:00Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "VA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "DC"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "WA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3333ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3333\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Costa (for himself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the National Advisory Council on Nurse Education and Practice to examine and report on the growing nursing shortage across the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Magnifying Opportunities to Recruit and Educate Nurses Act or the MORE Nurses Act .\n#### 2. Examination of the growing nursing shortage\n##### (a) Duties\nThe National Advisory Council on Nurse Education and Practice established pursuant to section 851 of the Public Health Service Act ( 42 U.S.C. 297t ) (in this section referred to as the National Advisory Council ) shall\u2014\n**(1)**\nexamine, assess, and report on the United States nursing workforce capacity, including\u2014\n**(A)**\ntrends in the overall nursing workforce;\n**(B)**\nthe capacity to educate future nurses;\n**(C)**\ncauses for the existing nursing shortage; and\n**(D)**\nFederal policies to bolster nursing education and the nursing workforce;\n**(2)**\nbuild upon existing or ongoing evaluations, and avoid unnecessary duplication, by reviewing, as appropriate, the findings, conclusions, and recommendations of other task forces, committees, commissions, and other public and private entities with respect to the national nursing shortage;\n**(3)**\nidentify areas of Federal policy that have impacted the ability of the United States to respond to the growing nursing shortage, including\u2014\n**(A)**\nFederal support of nursing education programs;\n**(B)**\nFederal support of increasing diversity in the nursing workforce; and\n**(C)**\nincentives for nurses to work in underserved areas and communities; and\n**(4)**\nidentify and recommend a set of possible solutions to the nursing shortage for policymakers, including legislative and regulatory recommendations.\n##### (b) Report\n**(1) Submission**\nNot later than one year after the date of enactment of this Act, the National Advisory Council shall\u2014\n**(A)**\ncomplete the activities required by subsection (a); and\n**(B)**\nsubmit to the President, the Congress, and the Secretary of Health and Human Services a report on the National Advisory Council\u2019s findings, conclusions, and recommendations to bolster nursing education and the nursing workforce in the United States.\n**(2) Public availability**\nThe National Advisory Council shall make the report required by paragraph (1) available to the public online.",
      "versionDate": "2025-05-13",
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
        "updateDate": "2025-05-27T14:21:30Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3333ih.xml"
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
      "title": "MORE Nurses Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MORE Nurses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Magnifying Opportunities to Recruit and Educate Nurses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the National Advisory Council on Nurse Education and Practice to examine and report on the growing nursing shortage across the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:19Z"
    }
  ]
}
```
