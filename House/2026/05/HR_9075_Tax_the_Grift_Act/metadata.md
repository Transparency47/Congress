# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9075?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9075
- Title: Tax the Grift Act
- Congress: 119
- Bill type: HR
- Bill number: 9075
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:23:28Z
- Update date including text: 2026-05-30T09:28:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-05-29: Introduced in House

## Actions

- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-29",
    "latestAction": {
      "actionDate": "2026-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9075",
    "number": "9075",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "P000607",
        "district": "2",
        "firstName": "Mark",
        "fullName": "Rep. Pocan, Mark [D-WI-2]",
        "lastName": "Pocan",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Tax the Grift Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:23:28Z",
    "updateDateIncludingText": "2026-05-30T09:28:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-29",
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
      "actionDate": "2026-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-29",
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
          "date": "2026-05-29T16:01:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr9075ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 9075\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2026 Mr. Pocan introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose a tax on payments received from any settlement fund established as a result of a civil action filed by the President of the United States against the Internal Revenue Service.\n#### 1. Short title\nThis Act may be cited as the Tax the Grift Act .\n#### 2. Imposition of tax on qualified settlement fund payments\n##### (a) In general\nSubtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new chapter:\n50B Qualified settlement fund payments Sec. 5000E. Imposition of tax on qualified settlement fund payments. 5000E. Imposition of tax on qualified settlement fund payments (a) In general There is hereby imposed on any taxpayer for any taxable year a tax equal to 100 percent of any qualified settlement fund payment received by such taxpayer during such taxable year. (b) Qualified settlement fund payment For purposes of this section, the term qualified settlement fund payment means, with respect to any taxpayer for any taxable year, any amount received by such taxpayer during such taxable year from any fund established as a result of a civil action filed by the President of the United States against the Internal Revenue Service. (c) Special rules (1) Administrative provisions For purposes of subtitle F, any tax imposed by this section shall be treated as a tax imposed by subtitle A. (2) Exclusion from gross income For purposes of chapter 1, the gross income of any taxpayer for any taxable year shall not include any qualified settlement fund payment received by such taxpayer during such taxable year. .\n##### (b) No deduction from income tax\nSection 275(a)(6) of such Code is amended by inserting 50B, after 50A, .\n##### (c) Clerical amendment\nThe table of chapters for subtitle D of such Code is amended by inserting after the item relating to chapter 50A the following new item:\nChapter 50B\u2014 Qualified settlement fund payments. .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to amounts received after the date of the enactment of this Act.",
      "versionDate": "2026-05-29",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr9075ih.xml"
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
      "title": "Tax the Grift Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tax the Grift Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to impose a tax on payments received from any settlement fund established as a result of a civil action filed by the President of the United States against the Internal Revenue Service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:18:34Z"
    }
  ]
}
```
