# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1859?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1859
- Title: Apprenticeship Opportunity Act
- Congress: 119
- Bill type: HR
- Bill number: 1859
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-04-28T08:06:12Z
- Update date including text: 2026-04-28T08:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1859",
    "number": "1859",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "D000617",
        "district": "1",
        "firstName": "Suzan",
        "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
        "lastName": "DelBene",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Apprenticeship Opportunity Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:12Z",
    "updateDateIncludingText": "2026-04-28T08:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:00:35Z",
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
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "WA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "WA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1859ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1859\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Ms. DelBene (for herself, Ms. S\u00e1nchez , Ms. Sewell , and Ms. Strickland ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require income from the first year of an apprenticeship to be disregarded in determining eligibility for assistance under the program of block grants to States for temporary assistance for needy families.\n#### 1. Short title\nThis Act may be cited as the Apprenticeship Opportunity Act .\n#### 2. Requirement to disregard income from first year of an apprenticeship in determining eligibility for assistance under the TANF program\n##### (a) Requirement\nSection 408(a) of the Social Security Act ( 42 U.S.C. 608(a) ) is amended by adding at the end the following:\n(13) Requirement to disregard income from 1st year of an apprenticeship in determining eligibility for assistance A State to which a grant is made under section 403 shall disregard all income received on account of the 1st year of an apprenticeship registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), in determining the eligibility of the recipient for assistance under the State program funded under this part. .\n##### (b) Penalty for violation\nSection 409(a) of such Act ( 42 U.S.C. 609(a) ) is amended by adding at the end the following:\n(17) Penalty for not disregarding income from 1st year of an apprenticeship in determining eligibility for assistance If the Secretary determines that a State to which a grant is made under section 403 in a fiscal year has violated section 408(a)(13) during the fiscal year, the Secretary shall reduce the grant payable to the State under section 403(a)(1) for the immediately succeeding fiscal year by an amount equal to 1 percent of the State family assistance grant. .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the 1st day of the 1st Federal fiscal year that begins after the date of the enactment of this Act.",
      "versionDate": "2025-03-05",
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
        "name": "Social Welfare",
        "updateDate": "2025-03-21T15:55:01Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1859ih.xml"
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
      "title": "Apprenticeship Opportunity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:10Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Apprenticeship Opportunity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require income from the first year of an apprenticeship to be disregarded in determining eligibility for assistance under the program of block grants to States for temporary assistance for needy families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T03:48:21Z"
    }
  ]
}
```
