# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3857?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3857
- Title: One Nation, One Visa Policy Act
- Congress: 119
- Bill type: S
- Bill number: 3857
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-05-15T11:03:25Z
- Update date including text: 2026-05-15T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3857",
    "number": "3857",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "One Nation, One Visa Policy Act",
    "type": "S",
    "updateDate": "2026-05-15T11:03:25Z",
    "updateDateIncludingText": "2026-05-15T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T17:34:59Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "UT"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3857is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3857\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit the Secretary of Homeland Security from admitting to the United States any national of the People's Republic of China without a valid visa, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Nation, One Visa Policy Act .\n#### 2. Prohibition on visa-free admission of Chinese nationals\n##### (a) In general\nThe Secretary of Homeland Security shall not admit any national of the People's Republic of China, or any individual bearing a passport issued by the People's Republic of China, who is not in possession of a valid visa.\n##### (b) Prohibition on use of funds\nNo funds appropriated or otherwise made available to the Department of Homeland Security may be used to allow the participation of any national of the People's Republic of China in the Guam and Commonwealth of the Northern Mariana Islands Visa Waiver Program authorized by section 212(l) of the Immigration and Nationality Act ( 8 U.S.C. 1182(l) ), including the Economic Vitality & Security Travel Authorization Program, or any other program that authorizes the admission of nationals of the People's Republic of China without a valid visa.\n##### (c) Definitions\nIn this section:\n**(1) In general**\nExcept as otherwise explicitly provided, a term used in this section shall have the meaning given such term in the immigration laws.\n**(2) Immigration laws**\nThe term immigration laws has the meaning given the term in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ).\n**(3) People's Republic of China**\nThe term People's Republic of China includes the Special Administrative Unit of Hong Kong and the Special Administrative Unit of Macau.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-03-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7780",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "One Nation, One Visa Policy Act",
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
        "name": "Immigration",
        "updateDate": "2026-03-02T18:26:41Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3857is.xml"
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
      "title": "One Nation, One Visa Policy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "One Nation, One Visa Policy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Secretary of Homeland Security from admitting to the United States any national of the People's Republic of China without a valid visa, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T03:48:23Z"
    }
  ]
}
```
