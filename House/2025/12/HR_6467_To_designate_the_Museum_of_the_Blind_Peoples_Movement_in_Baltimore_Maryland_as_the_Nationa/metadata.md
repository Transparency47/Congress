# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6467?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6467
- Title: National Museum of the Blind People’s Movement Act
- Congress: 119
- Bill type: HR
- Bill number: 6467
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-01T08:08:52Z
- Update date including text: 2026-05-01T08:08:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6467",
    "number": "6467",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "M000687",
        "district": "7",
        "firstName": "Kweisi",
        "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
        "lastName": "Mfume",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "National Museum of the Blind People\u2019s Movement Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:52Z",
    "updateDateIncludingText": "2026-05-01T08:08:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MD"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "DC"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "GA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IN"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "MD"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "MD"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "MD"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MD"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6467ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6467\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Mfume (for himself, Ms. Simon , Ms. Elfreth , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo designate the Museum of the Blind People\u2019s Movement in Baltimore, Maryland, as the National Museum of the Blind People\u2019s Movement .\n#### 1. Short title\nThis Act may be cited as the National Museum of the Blind People\u2019s Movement Act .\n#### 2. Designation of National Museum of the Blind People\u2019s Movement\n##### (a) Findings\nCongress finds the following:\n**(1)**\nEqual treatment under the law and equal access to all the rights, privileges, and protections of the Constitution are core tenets of the philosophy of the United States of America.\n**(2)**\nThose noble and lofty ideals have not always been met throughout the course of this country\u2019s shared national history and its movement toward a more perfect Union.\n**(3)**\nPeople with disabilities have faced unique challenges pertaining to accessibility and civil rights.\n**(4)**\nBlind individuals have experienced systemic discrimination and low expectations but, despite these barriers, have historically made significant contributions to society which have often gone underrecognized.\n**(5)**\nBlind people self-organized on a national basis in 1940 to establish the National Federation of the Blind which has served as a vehicle for collective action by the blind themselves to raise expectations in society.\n**(6)**\nThe National Federation of the Blind has served as the model and inspiration for the development of blind-led organizations the world over and sparked the creation of the International Federation of the Blind which later became part of the World Blind Union.\n**(7)**\nThroughout the course of its eight-decade crusade to ensure the full integration of the blind into society on the basis of equality, the National Federation of the Blind has acquired innumerable artifacts, documents, and literature detailing the individual and collective accomplishments and struggles of blind people and how those individuals have contributed to the broader American society.\n**(8)**\nThe United States has no cultural institution that centers the experience of blind people and elevates the understanding of how those individuals have worked together to improve society and to change the negative misconceptions about the blind in the Nation and around the world.\n**(9)**\nThe National Federation of the Blind has chosen to commit to the collection, preservation, and curation of this history through the Museum of the Blind People\u2019s Movement located inside the National Federation of the Blind Jernigan Institute in Baltimore, Maryland.\n**(10)**\nThis will be the first museum owned and operated by the blind of America.\n**(11)**\nThe museum, as well as the existing archive which is currently available to researchers, will serve as a national platform to explore the struggles and successes of the blind as individuals, as collectives, and as a movement, and to encourage understanding of the past, and facilitate awareness and evoke dialogue in the present, while inspiring respect, determination, and action for an equitable future.\n##### (b) Designation\nThe museum known as the Museum of the Blind People\u2019s Movement, located at 200 East Wells Street in Baltimore, Maryland, is designated as the National Museum of the Blind People\u2019s Movement .",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "3371",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "National Museum of the Blind People\u2019s Movement Act",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2026-01-07T17:20:04Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6467ih.xml"
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
      "title": "National Museum of the Blind People\u2019s Movement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Museum of the Blind People\u2019s Movement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate the Museum of the Blind People's Movement in Baltimore, Maryland, as the \"National Museum of the Blind People's Movement\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:26Z"
    }
  ]
}
```
