# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/638?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/638
- Title: A bill to amend the Act of June 22, 1948.
- Congress: 119
- Bill type: S
- Bill number: 638
- Origin chamber: Senate
- Introduced date: 2025-02-19
- Update date: 2025-12-12T16:33:17Z
- Update date including text: 2025-12-12T16:33:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-19: Introduced in Senate
- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 208.
- Latest action: 2025-02-19: Introduced in Senate

## Actions

- 2025-02-19 - IntroReferral: Introduced in Senate
- 2025-02-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 208.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-19",
    "latestAction": {
      "actionDate": "2025-02-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/638",
    "number": "638",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A bill to amend the Act of June 22, 1948.",
    "type": "S",
    "updateDate": "2025-12-12T16:33:17Z",
    "updateDateIncludingText": "2025-12-12T16:33:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-27",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 208.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-19",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-19",
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
        "item": [
          {
            "date": "2025-10-27T22:35:52Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-21T20:01:05Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-19T22:16:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s638is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 638\nIN THE SENATE OF THE UNITED STATES\nFebruary 19, 2025 Ms. Smith (for herself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Act of June 22, 1948.\n#### 1. Appraisals\nSection 5 of the Act of June 22, 1948 (commonly known as the Thye-Blatnik Act ) (62 Stat. 570, chapter 593; 16 U.S.C. 577g ), is amended by striking of the fair appraised value of such and inserting of the highest fair appraised value, including historical fair appraised values, as determined by the Secretary of Agriculture in accordance with this section, of such .",
      "versionDate": "2025-02-19",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s638rs.xml",
      "text": "II\nCalendar No. 208\n119th CONGRESS\n1st Session\nS. 638\nIN THE SENATE OF THE UNITED STATES\nFebruary 19, 2025 Ms. Smith (for herself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nOctober 27, 2025 Reported by Mr. Boozman , without amendment\nA BILL\nTo amend the Act of June 22, 1948.\n#### 1. Appraisals\nSection 5 of the Act of June 22, 1948 (commonly known as the Thye-Blatnik Act ) (62 Stat. 570, chapter 593; 16 U.S.C. 577g ), is amended by striking of the fair appraised value of such and inserting of the highest fair appraised value, including historical fair appraised values, as determined by the Secretary of Agriculture in accordance with this section, of such .",
      "versionDate": "2025-10-27",
      "versionType": "Reported in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Minnesota",
            "updateDate": "2025-08-13T18:31:13Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-08-13T18:31:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-12T16:33:16Z"
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
      "date": "2025-02-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s638is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s638rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Act of June 22, 1948.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:18:19Z"
    },
    {
      "title": "A bill to amend the Act of June 22, 1948.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T11:56:16Z"
    }
  ]
}
```
