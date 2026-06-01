# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3988?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3988
- Title: Veterans STAND Act
- Congress: 119
- Bill type: S
- Bill number: 3988
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3988",
    "number": "3988",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Veterans STAND Act",
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
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
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
            "date": "2026-04-29T21:37:30Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-04T18:34:04Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3988is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3988\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Moran introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to offer annual preventative health evaluations to veterans with a spinal cord injury or disorder and increase access to assistive technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Spinal Trauma Access to New Devices Act or the Veterans STAND Act .\n#### 2. Provision of preventative health evaluations for veterans with a spinal cord injury or disorder\nSection 1706 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(d) (1) In managing the provision of hospital care and medical services under section 1710(a) of this title, the Secretary shall furnish (through direct provision of service, referral, or a telehealth program operated by the Department) a preventative health evaluation annually to any veteran with a spinal cord injury or disorder who elects to undergo the evaluation. (2) The evaluation described in paragraph (1) shall include the following: (A) An assessment of any circumstance or condition the veteran is experiencing that indicates a risk for any health complication related to the spinal cord injury or disorder, including a risk of comorbidities. (B) An assessment regarding chronic pain and, if applicable, the management of chronic pain. (C) An assessment regarding dietary management and weight management. (D) An assessment regarding prosthetic equipment, including which prosthetic equipment the veteran needs, how well any existing prosthetic equipment is functioning considering the needs of the veteran, and any safety concerns regarding the prosthetic equipment in use by or recommended to the veteran. (E) An assessment with respect to the provision of assistive technology, including spinal cord neuromodulation technology (such as non-invasive transcutaneous spinal stimulation), that could help maximize the voluntary motor or autonomic function, independence, or mobility of the veteran, including suitability of such technology for home use and need for training, programming, and remote follow-up. (3) (A) In maintaining, prescribing, or amending any guidance, rules, or regulations issued by the Department regarding the requirements set out in this subsection, the Secretary shall consult with\u2014 (i) the spinal cord injury and disorder program managers of the Department; (ii) clinicians employed by the Department as specialists in spinal cord injuries and disorders; (iii) clinicians and technologists with demonstrated expertise in spinal cord neuromodulation therapies, including non-invasive transcutaneous approaches; and (iv) representatives of organizations recognized under section 5902 of this title. (B) Before issuing any guidance, rules, or regulations regarding the requirements set out in this subsection, the Secretary shall consult with manufacturers of assistive technologies and other entities relevant to the provision of assistive technologies if the guidance, rules, or regulations would directly affect such manufacturers or entities. (C) The Secretary shall ensure, to the extent possible, that any veteran known by the Secretary to have a spinal cord injury or disorder receives information annually about the evaluation available under this subsection and the benefits to the veteran of choosing to undergo the evaluation. (4) As the Secretary determines clinically appropriate, the Secretary may provide training, programming, remote monitoring, and follow-up for assistive technologies through telehealth. (5) Not later than one year after the date of the enactment of the Veterans Spinal Trauma Access to New Devices Act , and every two years thereafter, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report that includes the following: (A) For the period covered by the report\u2014 (i) the number of veterans who\u2014 (I) received hospital care or medical services from the Department and used an assistive technology; (II) received hospital care or medical services from the Department and were assessed for the provision of an assistive technology; and (III) received hospital care or medical services from the Department and were prescribed an assistive technology. (ii) for any assistive technology prescribed, an identification of the category of such technology, including spinal cord neuromodulation, and a summary of functional outcomes associated with the prescription of such technology, if available. (B) The year-to-year change (for the period covered by the report, including the two years immediately prior to year the report is submitted) in the percent of veterans with a spinal cord injury or disorder who received an evaluation under this subsection. (6) In reviewing the performance metrics of a Veterans Integrated Service Network for any year beginning after the date that is one year after the date of the enactment of the Veterans Spinal Trauma Access to New Devices Act , the Secretary shall consider the provision of evaluations under paragraph (1). (7) In this subsection, the term assistive technology means a powered medical device or electronic tool used to treat or alleviate symptoms or conditions caused by a spinal cord injury or disorder, including the following: (A) A personal mobility device, including a powered exoskeleton device. (B) A speech generating device. (C) A spinal cord neuromodulation technology, including non-invasive transcutaneous spinal stimulation using sensory (afferent) pathways, intended to improve voluntary motor function, autonomic function, independence, or quality of life. (D) As clinically appropriate, and consistent with the prosthetic and sensory aids policies of the Department, an implantable spinal cord stimulation system that is approved by the Food and Drug Administration. .",
      "versionDate": "2026-03-04",
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
        "actionDate": "2026-02-12",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "6835",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans STAND Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-20T15:32:14Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3988is.xml"
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
      "title": "Veterans STAND Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans STAND Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Spinal Trauma Access to New Devices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to direct the Secretary of Veterans Affairs to offer annual preventative health evaluations to veterans with a spinal cord injury or disorder and increase access to assistive technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:51Z"
    }
  ]
}
```
