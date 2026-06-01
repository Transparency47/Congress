# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2745
- Title: Federal Firefighter Cancer Detection and Prevention Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2745
- Origin chamber: Senate
- Introduced date: 2025-09-09
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in Senate
- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-09-09: Introduced in Senate

## Actions

- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2745",
    "number": "2745",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001208",
        "district": "",
        "firstName": "Elissa",
        "fullName": "Sen. Slotkin, Elissa [D-MI]",
        "lastName": "Slotkin",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Federal Firefighter Cancer Detection and Prevention Act of 2025",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-09",
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
            "date": "2025-09-09T21:07:30Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-09T21:07:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "ME"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2745is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2745\nIN THE SENATE OF THE UNITED STATES\nSeptember 9, 2025 Ms. Slotkin (for herself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of Defense to provide to firefighters of the Department of Defense medical testing and related services to detect and prevent certain cancers.\n#### 1. Short title\nThis Act may be cited as the Federal Firefighter Cancer Detection and Prevention Act of 2025 .\n#### 2. Medical testing and related services for firefighters of Department of Defense\n##### (a) Provision of services\nDuring the annual periodic health assessment of each firefighter of the Department of Defense, or at such other intervals as may be indicated in subsection (b), the Secretary of Defense shall provide to the firefighter (at no cost to the firefighter) appropriate medical testing and related services to detect, document the presence or absence of, and prevent, certain cancers.\n##### (b) Criteria\nServices required to be provided under subsection (a) shall meet, at a minimum, the following criteria:\n**(1) Breast cancer**\nWith respect to breast cancer screening, if the firefighter is a female firefighter\u2014\n**(A)**\nsuch services shall include the provision of a mammogram to the firefighter\u2014\n**(i)**\nif the firefighter is 40 years old to 49 years old (inclusive), not less frequently than twice each year;\n**(ii)**\nif the firefighter is 50 years old or older, not less frequently than annually; and\n**(iii)**\nas clinically indicated (without regard to age); and\n**(B)**\nin connection with the provision of a mammogram under subparagraph (A), a licensed radiologist shall review the most recent mammogram provided to the firefighter, as compared to prior mammograms so provided, and provide to the firefighter the results of such review.\n**(2) Colon cancer**\nWith respect to colon cancer screening\u2014\n**(A)**\nif the firefighter is 40 years old or older, or as clinically indicated without regard to age, such services shall include the communication to the firefighter of the risks and benefits of stool-based blood testing;\n**(B)**\nif the firefighter is 45 years old or older, or as clinically indicated without regard to age, such services shall include the provision, at regular intervals, of visual examinations (such as a colonoscopy, CT colonoscopy, or flexible sigmoidoscopy) or stool-based blood testing; and\n**(C)**\nin connection with the provision of a visual examination or stool-based blood testing under subparagraph (B), a licensed physician shall review and provide to the firefighter the results of such examination or testing, as the case may be.\n**(3) Prostate cancer**\nWith respect to prostate cancer screening, if the firefighter is a male firefighter, such services shall include the communication to the firefighter of the risks and benefits of prostate cancer screenings and the provision to the firefighter of a prostate-specific antigen test\u2014\n**(A)**\nnot less frequently than annually if the firefighter\u2014\n**(i)**\nis 50 years old or older; or\n**(ii)**\nis 40 years old or older and is a high-risk individual; and\n**(B)**\nas clinically indicated (without regard to age).\n**(4) Other cancers**\nSuch services shall include routine screenings for any other cancer the risk or occurrence of which the Director of the Centers for Disease Control and Prevention has identified as higher among firefighters than among the general public, the provision of which shall be carried out during the annual periodic health assessment of the firefighter.\n##### (c) Optional nature\nA firefighter of the Department of Defense may opt out of the receipt of medical testing or a related service provided under subsection (a).\n##### (d) Use of consensus technical standards\nIn providing medical testing and related services under subsection (a), the Secretary shall use consensus technical standards in accordance with section 12(d) of the National Technology Transfer and Advancement Act of 1995 ( Public Law 104\u2013113 ; 15 U.S.C. 272 note).\n##### (e) Documentation\n**(1) In general**\nIn providing medical testing and related services under subsection (a), the Secretary\u2014\n**(A)**\nshall document the acceptance rates of such tests offered and the rates of such tests performed;\n**(B)**\nshall document test results to identify trends in the rates of cancer occurrences among firefighters; and\n**(C)**\nmay collect and maintain additional information from the recipients of such tests and other services to allow for appropriate scientific analysis.\n**(2) Privacy**\nIn analyzing any information of an individual documented, collected, or maintained under paragraph (1), in addition to complying with other applicable privacy laws, the Secretary shall ensure the name and any other personally identifiable information of the individual is removed from such information prior to the analysis.\n**(3) Sharing with Centers for Disease Control and Prevention**\nThe Secretary may share data from any tests performed under subsection (a) with the Director of the Centers for Disease Control and Prevention, as appropriate, to increase the knowledge and understanding of cancer occurrences among firefighters.\n##### (f) Definitions\nIn this section:\n**(1) Firefighter**\nThe term firefighter means someone whose primary job or military occupational specialty is being a firefighter.\n**(2) High-risk individual**\nThe term high-risk individual means an individual who\u2014\n**(A)**\nis African American;\n**(B)**\nhas at least one first-degree relative who has been diagnosed with prostate cancer at an early age; or\n**(C)**\nis otherwise determined by the Secretary to be high risk with respect to prostate cancer.",
      "versionDate": "2025-09-09",
      "versionType": "Introduced in Senate"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-23T18:27:58Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2745is.xml"
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
      "title": "Federal Firefighter Cancer Detection and Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Firefighter Cancer Detection and Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-17T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Defense to provide to firefighters of the Department of Defense medical testing and related services to detect and prevent certain cancers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T02:48:28Z"
    }
  ]
}
```
