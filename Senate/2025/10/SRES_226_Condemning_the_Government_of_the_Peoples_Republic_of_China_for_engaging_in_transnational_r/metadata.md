# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/226?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/226
- Title: A resolution condemning the Government of the People's Republic of China for engaging in transnational repression.
- Congress: 119
- Bill type: SRES
- Bill number: 226
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2025-12-17T17:31:04Z
- Update date including text: 2025-12-17T17:31:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2930-2931)
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and with an amended preamble. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and with an amended preamble. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 247.
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2930-2931)
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and with an amended preamble. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and with an amended preamble. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 247.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/226",
    "number": "226",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "A resolution condemning the Government of the People's Republic of China for engaging in transnational repression.",
    "type": "SRES",
    "updateDate": "2025-12-17T17:31:04Z",
    "updateDateIncludingText": "2025-12-17T17:31:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 247.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and with an amended preamble. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and with an amended preamble. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S2930-2931)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-14",
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
            "date": "2025-10-30T15:46:27Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T15:13:28Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-14T18:09:19Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "AK"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres226is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 226\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Merkley (for himself, Mr. Sullivan , and Mr. Curtis ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCondemning the Government of the People\u2019s Republic of China for engaging in transnational repression.\nThat the Senate\u2014\n**(1)**\ncondemns the Government of the People\u2019s Republic of China for its systematic campaign of transnational repression;\n**(2)**\naffirms that all individuals residing in the United States have the right to live free from foreign government intimidation, coercion, and surveillance;\n**(3)**\ndeclares that acts of transnational repression carried out by the Government of the People\u2019s Republic of China in the United States violate our Nation's sovereignty and democratic values;\n**(4)**\nrecognizes that the Government of the People\u2019s Republic of China\u2019s harassment, threats, or unlawful detention of the family members of such individuals who are residing in the People's Republic of China or regions controlled by the Government of the People's Republic of China is an extension of this repression and a violation of basic human rights; and\n**(5)**\nsupports efforts by the United States Government to investigate, disrupt, and hold accountable those who carry out or enable such activities.",
      "versionDate": "2025-05-14",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres226rs.xml",
      "text": "III\nCalendar No. 247\n119th CONGRESS\n1st Session\nS. RES. 226\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Merkley (for himself, Mr. Sullivan , and Mr. Curtis ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , with an amendment and an amendment to the preamble Strike out all after the resolving clause and insert the part printed in italic Strike the preamble and insert the part printed in italic\nRESOLUTION\nCondemning the Government of the People\u2019s Republic of China for engaging in transnational repression.\nThat the Senate\u2014\n**(1)**\ncondemns the Government of the People\u2019s Republic of China for its systematic campaign of transnational repression;\n**(2)**\naffirms that all individuals residing in the United States have the right to live free from foreign government intimidation, coercion, and surveillance;\n**(3)**\ndeclares that acts of transnational repression carried out by the Government of the People\u2019s Republic of China in the United States violate our Nation's sovereignty and democratic values;\n**(4)**\nrecognizes that the Government of the People\u2019s Republic of China\u2019s harassment, threats, or unlawful detention of the family members of such individuals who are residing in the People's Republic of China or regions controlled by the Government of the People's Republic of China is an extension of this repression and a violation of basic human rights; and\n**(5)**\nsupports efforts by the United States Government to investigate, disrupt, and hold accountable those who carry out or enable such activities.",
      "versionDate": "2025-10-30",
      "versionType": "RS"
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
            "name": "Asia",
            "updateDate": "2025-12-17T17:30:20Z"
          },
          {
            "name": "China",
            "updateDate": "2025-12-17T17:30:08Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-12-17T17:30:43Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-12-17T17:30:29Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-12-17T17:30:35Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-12-17T17:30:14Z"
          },
          {
            "name": "Refugees, asylum, displaced persons",
            "updateDate": "2025-12-17T17:30:53Z"
          },
          {
            "name": "Rule of law and government transparency",
            "updateDate": "2025-12-17T17:31:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-06-10T15:02:02Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres226is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres226rs.xml"
        }
      ],
      "type": "RS"
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
      "title": "A resolution condemning the Government of the People's Republic of China for engaging in transnational repression.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T03:18:28Z"
    },
    {
      "title": "A resolution condemning the Government of the People's Republic of China for engaging in transnational repression.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T10:56:24Z"
    }
  ]
}
```
