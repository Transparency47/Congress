# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/132
- Title: A resolution designating March 24, 2025, as "National Women of Color in Tech Day".
- Congress: 119
- Bill type: SRES
- Bill number: 132
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1805)
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1805)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/132",
    "number": "132",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "A resolution designating March 24, 2025, as \"National Women of Color in Tech Day\".",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1805)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T20:26:27Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "HI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MN"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NV"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres132is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 132\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Ms. Rosen (for herself, Mr. Padilla , Ms. Hirono , Ms. Klobuchar , Mr. Fetterman , Ms. Cortez Masto , Mr. Blumenthal , and Mr. Schiff ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating March 24, 2025, as National Women of Color in Tech Day .\nThat the Senate\u2014\n**(1)**\ndesignates March 24, 2025, as National Women of Color in Tech Day ;\n**(2)**\nrecognizes the celebration of National Women of Color in Tech Day as a time to reflect on the many notable contributions that women of color have made to the field of technology in the United States;\n**(3)**\nurges the people of the United States to observe National Women of Color in Tech Day with appropriate programs and activities;\n**(4)**\npledges to work to increase diversity and inclusion in the technology sector, including through robust plans to ensure recruitment, training, and retention of underrepresented minorities at all levels;\n**(5)**\ncommits to working to eliminate barriers to entering the technology sector faced by women of color and individuals from other underrepresented groups;\n**(6)**\nreaffirms the commitment of the Senate to ensuring that all students have access to science, technology, engineering, and mathematics (referred to in this resolution as STEM ) education for a 21st-century economy, including computer science education in particular;\n**(7)**\nsupports efforts to strengthen investments in, and collaborations with, educational institutions, including community colleges, historically Black colleges and universities, Hispanic-serving institutions, Asian-American, Native American, and Pacific Islander-serving institutions, Tribal Colleges and Universities, Alaska Native and Native Hawaiian-serving institutions, and other minority-serving institutions, to sustain a pipeline of diverse STEM graduates ready to enter the technology sector; and\n**(8)**\nurges the President to work with Congress to improve data collection, data disaggregation, and dissemination of information for greater understanding and transparency of diversity in STEM education and across the workforce of the United States.",
      "versionDate": "2025-03-24",
      "versionType": "IS"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-06T19:43:13Z"
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
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres132is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution designating March 24, 2025, as \"National Women of Color in Tech Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T11:33:21Z"
    },
    {
      "title": "A resolution designating March 24, 2025, as \"National Women of Color in Tech Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T10:56:22Z"
    }
  ]
}
```
