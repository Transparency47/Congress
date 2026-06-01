# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4089?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4089
- Title: Supporting Blue Envelope Programs Act
- Congress: 119
- Bill type: S
- Bill number: 4089
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-04-02T13:30:51Z
- Update date including text: 2026-04-02T13:30:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4089",
    "number": "4089",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "Supporting Blue Envelope Programs Act",
    "type": "S",
    "updateDate": "2026-04-02T13:30:51Z",
    "updateDateIncludingText": "2026-04-02T13:30:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T17:47:05Z",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4089is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4089\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Coons (for himself and Mr. Schmitt ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize the Attorney General to make grants to eligible entities to carry out blue envelope programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Blue Envelope Programs Act .\n#### 2. Blue envelope grant program\n##### (a) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na law enforcement agency or group of law enforcement agencies that has a partnership with a nonprofit organization described in subparagraph (B) for the purpose of creating or supporting a blue envelope program; or\n**(B)**\na nonprofit organization\u2014\n**(i)**\nthat provides services to or otherwise assists individuals with autism spectrum disorder or developmental, cognitive, sensory, or communication disabilities, and families of those individuals; and\n**(ii)**\nthat has a partnership with not fewer than 1 law enforcement agency for the purpose of creating or supporting a blue envelope program.\n**(2) Blue envelope program**\nThe term blue envelope program means a program operated by an eligible entity\u2014\n**(A)**\nthat provides training, including crisis response and deescalation tactic training, and resources for law enforcement officers (and may provide training for first responders) on improving interactions with individuals with autism spectrum disorder or developmental, cognitive, sensory, or communication disabilities;\n**(B)**\nthat does not have a registration component or participant list for participating individuals described in subparagraph (A);\n**(C)**\nin which participation is voluntary for individuals described in subparagraph (A);\n**(D)**\nthat provides individuals described in subparagraph (A) with items and materials that help overcome communication barriers in interactions with law enforcement and first responders, including\u2014\n**(i)**\nblue envelopes that can be used to store essential documents in vehicles, such as identification, diagnosis information, communication preferences and emergency contact information for use during vehicle-related law enforcement encounters; and\n**(ii)**\nother items and materials that may include\u2014\n**(I)**\ncar decals;\n**(II)**\nseatbealt covers;\n**(III)**\nlanyards;\n**(IV)**\nkeychains;\n**(V)**\npins; and\n**(VI)**\nother accessories and resources that can be helpful in overcoming communication barriers in interactions with law enforcement and first responders; and\n**(E)**\nthat provides education, including voluntary training and resources\u2014\n**(i)**\nfor community members on how to safely interact with individuals described in subparagraph (A); and\n**(ii)**\nfor individuals described in subparagraph (A) on how use the items and materials described in subparagraph (D).\n**(3) Director**\nThe term Director means the Director of the Bureau of Justice Assistance.\n**(4) State; unit of local government**\nThe terms State and unit of local government have the meanings given those terms in section 901 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251 ).\n##### (b) Establishment\nThe Attorney General, acting through the Director, may make grants to eligible entities to create or support blue envelope programs.\n##### (c) Priority\nIn awarding grants under this section, the Director shall prioritize blue envelope programs that\u2014\n**(1)**\nhave scalability or a plan to continue the operation of the program beyond the duration of the grant award;\n**(2)**\nhave community support;\n**(3)**\ninvolve multiple law enforcement agencies; and\n**(4)**\ninvolve entities that\u2014\n**(A)**\nhave demonstrated person-centered and trauma-informed practices and actively engage individuals in the community with autism spectrum disorder or developmental, cognitive, sensory, or communication disabilities, who may face communication barriers during law enforcement encounters;\n**(B)**\nhave experience in providing training and resources to law enforcement agencies in interactions with such individuals; and\n**(C)**\nseek the input and feedback from self-advocates with a variety of disabilities.\n##### (d) Distribution\nThe Director shall make every effort to\u2014\n**(1)**\nensure a broad geographic distribution of awards under this section; and\n**(2)**\ntake into consideration the needs of underserved populations, including rural and Tribal communities.\n##### (e) Report\nOn the date that is 1 year after the date of enactment of this Act, and every 2 years thereafter, the Director shall submit to Congress a report on\u2014\n**(1)**\nthe implementation of the grant program under this section;\n**(2)**\ndifferent models and examples of blue envelope programs funded under this section, including trainings and materials used; and\n**(3)**\nrecommended best practices for blue envelope programs.\n##### (f) Directory\nThe Director shall maintain a publicly accessible online directory of blue envelope programs for use by members of the public to locate the nearest blue envelope program.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to the Attorney General to carry out this section $5,000,000 for each of fiscal years 2027 through 2031.",
      "versionDate": "2026-03-12",
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
        "actionDate": "2025-12-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6602",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting Blue Envelope Programs Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-30T19:45:57Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4089is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Attorney General to make grants to eligible entities to carry out blue envelope programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:35Z"
    },
    {
      "title": "Supporting Blue Envelope Programs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting Blue Envelope Programs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    }
  ]
}
```
