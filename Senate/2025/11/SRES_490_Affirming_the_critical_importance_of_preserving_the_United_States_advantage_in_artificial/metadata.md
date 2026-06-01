# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/490?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/490
- Title: A resolution affirming the critical importance of preserving the United States' advantage in artificial intelligence and ensuring that the United States achieves and maintains artificial intelligence dominance.
- Congress: 119
- Bill type: SRES
- Bill number: 490
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-11-19T17:04:30Z
- Update date including text: 2025-11-19T17:04:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Referred to the Committee on Foreign Relations.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/490",
    "number": "490",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
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
    "title": "A resolution affirming the critical importance of preserving the United States' advantage in artificial intelligence and ensuring that the United States achieves and maintains artificial intelligence dominance.",
    "type": "SRES",
    "updateDate": "2025-11-19T17:04:30Z",
    "updateDateIncludingText": "2025-11-19T17:04:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T23:05:06Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "AR"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "PA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NH"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres490is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 490\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Coons (for himself, Mr. Cotton , Mr. McCormick , and Ms. Klobuchar ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nAffirming the critical importance of preserving the United States' advantage in artificial intelligence and ensuring that the United States achieves and maintains artificial intelligence dominance.\nThat the Senate\u2014\n**(1)**\naffirms that the preservation of the United States\u2019 primacy in artificial intelligence is a national imperative that is critical to maintaining our global leadership, economic prosperity, and national security;\n**(2)**\ncommends the White House AI Action Plan, including its recognition that advanced AI compute is essential to the AI era, enabling both economic dynamism and novel military capabilities and that denying our foreign adversaries access to this resource, then, is a matter of both geostrategic competition and national security ;\n**(3)**\napplauds United States Government efforts to deny the Government of the People's Republic of China access to advanced chips and chipmaking equipment, and affirms the importance of continuing these efforts;\n**(4)**\nrecognizes that efforts of the Government of the People's Republic China to close the AI gap and leap ahead of the United States in developing frontier AI models, and deploy Chinese AI models for the world to use and build on, present a clear and imminent threat to the United States, and that China\u2019s self-acknowledged inability to make and access computing power is the main impediment to its progress;\n**(5)**\nemphasizes that the world\u2019s most powerful supercomputers and next generation of AI models must be built in the United States and by United States companies;\n**(6)**\ncalls on the United States Government to ensure that United States companies maintain priority access to the cutting-edge AI chips they require to build frontier AI models and are not deprioritized in favor of buyers in China or other arms-embargoed countries;\n**(7)**\nemphasizes the importance of exporting the full United States AI stack\u2014which includes United States AI chips, cloud infrastructure, and models\u2014to allies and partners, while restricting access to the most sophisticated chips and models that United States adversaries may seek to use against the United States, whether by enforcing export controls and countering illegal chip diversion or by strategically limiting legal exports of advanced chips to adversary countries; and\n**(8)**\nasserts the need to prioritize investments in the energy, telecommunications, and physical infrastructure necessary to enable widespread adoption of AI technology.",
      "versionDate": "2025-11-06",
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
        "name": "International Affairs",
        "updateDate": "2025-11-19T17:04:30Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres490is.xml"
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
      "title": "A resolution affirming the critical importance of preserving the United States' advantage in artificial intelligence and ensuring that the United States achieves and maintains artificial intelligence dominance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:26Z"
    },
    {
      "title": "A resolution affirming the critical importance of preserving the United States' advantage in artificial intelligence and ensuring that the United States achieves and maintains artificial intelligence dominance.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T11:56:22Z"
    }
  ]
}
```
