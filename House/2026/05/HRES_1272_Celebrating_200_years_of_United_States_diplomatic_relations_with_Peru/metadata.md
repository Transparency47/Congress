# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1272
- Title: Celebrating 200 years of United States diplomatic relations with Peru.
- Congress: 119
- Bill type: HRES
- Bill number: 1272
- Origin chamber: House
- Introduced date: 2026-05-11
- Update date: 2026-05-13T21:08:43Z
- Update date including text: 2026-05-13T21:08:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-11: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-11 - IntroReferral: Submitted in House
- Latest action: 2026-05-11: Submitted in House

## Actions

- 2026-05-11 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-11 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-11",
    "latestAction": {
      "actionDate": "2026-05-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1272",
    "number": "1272",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000593",
        "district": "28",
        "firstName": "Carlos",
        "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
        "lastName": "Gimenez",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Celebrating 200 years of United States diplomatic relations with Peru.",
    "type": "HRES",
    "updateDate": "2026-05-13T21:08:43Z",
    "updateDateIncludingText": "2026-05-13T21:08:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-05-11T14:31:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1272ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1272\nIN THE HOUSE OF REPRESENTATIVES\nMay 11, 2026 Mr. Gimenez (for himself and Mr. Garcia of California ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nCelebrating 200 years of United States diplomatic relations with Peru.\nThat the House of Representatives\u2014\n**(1)**\ncelebrates the 200th anniversary of diplomatic relations between the United States and Peru;\n**(2)**\nrecognizes Peru as a long standing critical partner in advancing stability, democracy, and prosperity in the Western Hemisphere;\n**(3)**\ncommends the contributions of Peruvian Americans to the social, cultural, and economic fabric of the United States;\n**(4)**\nreaffirms the commitment of the United States to deepen cooperation with Peru in pursuit of shared goals; and\n**(5)**\nencourages continued partnership to address shared regional and global challenges, including the defense of democratic institutions, regional security and stability, and economic prosperity, while also reaffirming the deep cultural, social, and people-to-people ties that have long strengthened the friendship between the United States and Peru.",
      "versionDate": "2026-05-11",
      "versionType": "IH"
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
        "name": "International Affairs",
        "updateDate": "2026-05-13T21:08:43Z"
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
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1272ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Celebrating 200 years of United States diplomatic relations with Peru.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T08:18:31Z"
    },
    {
      "title": "Celebrating 200 years of United States diplomatic relations with Peru.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T08:06:26Z"
    }
  ]
}
```
