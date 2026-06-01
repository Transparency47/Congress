# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1324?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1324
- Title: Recognizing the 1885 Rock Springs Chinese Massacre.
- Congress: 119
- Bill type: HRES
- Bill number: 1324
- Origin chamber: House
- Introduced date: 2026-05-26
- Update date: 2026-05-27T08:18:34Z
- Update date including text: 2026-05-27T08:18:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-26: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-26 - IntroReferral: Submitted in House
- Latest action: 2026-05-26: Submitted in House

## Actions

- 2026-05-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-26 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-26",
    "latestAction": {
      "actionDate": "2026-05-26",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1324",
    "number": "1324",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001080",
        "district": "28",
        "firstName": "Judy",
        "fullName": "Rep. Chu, Judy [D-CA-28]",
        "lastName": "Chu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Recognizing the 1885 Rock Springs Chinese Massacre.",
    "type": "HRES",
    "updateDate": "2026-05-27T08:18:34Z",
    "updateDateIncludingText": "2026-05-27T08:18:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-26",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
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
          "date": "2026-05-26T15:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-26T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "IL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "NY"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1324ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1324\nIN THE HOUSE OF REPRESENTATIVES\nMay 26, 2026 Ms. Chu (for herself, Ms. Meng , Mr. Khanna , Mr. Krishnamoorthi , Ms. Vel\u00e1zquez , Ms. Simon , Ms. Tlaib , and Ms. Norton ) submitted the following resolution; which was referred to the Committee on the Judiciary , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nRecognizing the 1885 Rock Springs Chinese Massacre.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the Rock Springs Chinese Massacre of 1885 and honors the memory of the Chinese immigrant workers who were murdered;\n**(2)**\nacknowledges the massacre as one of the deadliest acts of anti-Chinese and anti-immigrant violence in United States history;\n**(3)**\nhonors the contributions of Chinese immigrant laborers whose work helped build critical American infrastructure despite exploitation, discrimination, and violence;\n**(4)**\ncondemns the racist mob violence perpetrated against the Chinese community of Rock Springs and the failure of authorities to protect Chinese residents or hold perpetrators accountable;\n**(5)**\ncondemns historical efforts to erase, distort, or deny the reality of the Rock Springs Chinese Massacre and other acts of anti-Asian violence;\n**(6)**\nrecognizes the importance of education about the Rock Springs Chinese Massacre and the broader history of anti-Asian discrimination in the United States;\n**(7)**\nencourages the documentation, interpretation, and commemoration of the Rock Springs Chinese Massacre site in Wyoming, including through survey, historical research, archaeological excavations, and consideration of eligibility for recognition under Federal historic preservation programs, as part of a broader effort to identify and preserve places significant to the history of Chinese Americans and Asian and Pacific Islander American communities in the United States and as recommended in the Transcontinental Railroad Study approved by Congress in 2019;\n**(8)**\nencourages education about the Rock Springs Chinese Massacre, including its causes, the racial ideology that fueled it, and the subsequent attempts to deny or rewrite its history, in schools and institutions of higher education; and\n**(9)**\nrecognizes the responsibility of Congress to acknowledge and learn from the history of anti-Asian violence, discrimination, and exclusion in the United States, including the Rock Springs Chinese Massacre, and to work toward racial justice.",
      "versionDate": "2026-05-26",
      "versionType": "IH"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1324ih.xml"
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
      "title": "Recognizing the 1885 Rock Springs Chinese Massacre.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:18:34Z"
    },
    {
      "title": "Recognizing the 1885 Rock Springs Chinese Massacre.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:05:55Z"
    }
  ]
}
```
