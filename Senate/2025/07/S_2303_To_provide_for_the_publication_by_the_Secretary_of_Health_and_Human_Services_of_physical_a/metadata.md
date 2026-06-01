# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2303?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2303
- Title: Promoting Physical Activity for Americans Act
- Congress: 119
- Bill type: S
- Bill number: 2303
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2025-12-05T21:37:48Z
- Update date including text: 2025-12-05T21:37:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2303",
    "number": "2303",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000437",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Wicker, Roger F. [R-MS]",
        "lastName": "Wicker",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Promoting Physical Activity for Americans Act",
    "type": "S",
    "updateDate": "2025-12-05T21:37:48Z",
    "updateDateIncludingText": "2025-12-05T21:37:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T16:26:07Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2303is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2303\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Wicker (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide for the publication by the Secretary of Health and Human Services of physical activity recommendations for Americans.\n#### 1. Short title\nThis Act may be cited as the Promoting Physical Activity for Americans Act .\n#### 2. Physical activity recommendations for Americans\n##### (a) Reports\n**(1) In general**\nNot later than December 31, 2029, and at least every 10 years thereafter, the Secretary of Health and Human Services (referred to in this section as the Secretary ) shall publish a report that provides physical activity recommendations for the people of the United States. Each such report shall contain physical activity information and recommendations for consideration and use by the general public, and shall be considered, as applicable and appropriate, by relevant Federal agencies in carrying out relevant Federal health programs.\n**(2) Basis of recommendations**\nThe information contained in each report required under paragraph (1) shall be based on the most current evidence-based scientific and medical knowledge at the time the report is prepared, and shall include additional recommendations for population subgroups, such as children or individuals with disabilities, including information regarding engagement in appropriate physical activity and avoiding inactivity.\n**(3) Update reports**\nNot later than 5 years after the publication of the first report under paragraph (1), and at least every 10 years thereafter, the Secretary shall publish an updated report detailing evidence-based practices and highlighting continuing issues with respect to physical activity. The contents of reports under this paragraph may focus on a particular group, subsection, or other division of the general public or on a particular issue relating to physical activity.\n##### (b) Interaction with other recommendations\nFederal agencies proposing to issue physical activity recommendations that differ from the recommendations in the most recent report published under subsection (a)(1) shall, as applicable and appropriate, take into consideration the recommendations provided through reports issued under this Act.\n##### (c) Existing authority not affected\nThis section is not intended to limit the support of biomedical research by any Federal agency or to limit the presentation or communication of scientific or medical findings or review of such findings by any Federal agency.\n##### (d) Limitation\nNotwithstanding any other provision of this Act, no physical fitness standard established under this Act shall be binding on any individual as a matter of Federal law or regulation.",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-11-19",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6121",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Promoting Physical Activity for Americans Act",
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
        "updateDate": "2025-09-05T15:16:16Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2303is.xml"
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
      "title": "Promoting Physical Activity for Americans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Physical Activity for Americans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the publication by the Secretary of Health and Human Services of physical activity recommendations for Americans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:21Z"
    }
  ]
}
```
