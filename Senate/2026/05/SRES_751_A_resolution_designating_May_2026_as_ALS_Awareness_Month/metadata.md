# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/751?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/751
- Title: A resolution designating May 2026 as "ALS Awareness Month".
- Congress: 119
- Bill type: SRES
- Bill number: 751
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-23T06:48:31Z
- Update date including text: 2026-05-23T06:48:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2446-2447)
- 2026-05-21 - IntroReferral: Submitted in Senate
- Latest action: 2026-05-21: Submitted in Senate

## Actions

- 2026-05-21 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2446-2447)
- 2026-05-21 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/751",
    "number": "751",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "A resolution designating May 2026 as \"ALS Awareness Month\".",
    "type": "SRES",
    "updateDate": "2026-05-23T06:48:31Z",
    "updateDateIncludingText": "2026-05-23T06:48:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S2446-2447)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-05-21T18:13:32Z",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "AK"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "RI"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres751is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 751\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2026 Mr. Coons (for himself, Ms. Murkowski , Mr. Whitehouse , and Mr. Cotton ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating May 2026 as ALS Awareness Month .\nThat the Senate\u2014\n**(1)**\ndesignates May 2026 as ALS Awareness Month ;\n**(2)**\naffirms the dedication of the Senate to\u2014\n**(A)**\nensuring individuals with amyotrophic lateral sclerosis (referred to in this resolution as ALS ) have access to effective treatments and high-quality services and supports as early as possible after diagnosis;\n**(B)**\nidentifying risk factors and causes of ALS to prevent new cases;\n**(C)**\nempowering individuals with ALS to maintain their personal independence to the maximum extent possible; and\n**(D)**\nreducing the physical and emotional burdens of living with ALS; and\n**(3)**\ncommends the dedication of the family members, friends, organizations, volunteers, researchers, and caregivers across the United States who are working to improve the quality and length of life of ALS patients and develop treatments and cures that reach patients as soon as possible.",
      "versionDate": "2026-05-21",
      "versionType": "IS"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres751is.xml"
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
      "title": "A resolution designating May 2026 as \"ALS Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-23T06:48:31Z"
    },
    {
      "title": "A resolution designating May 2026 as \"ALS Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:36Z"
    }
  ]
}
```
