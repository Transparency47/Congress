# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6835?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6835
- Title: Veterans STAND Act
- Congress: 119
- Bill type: HR
- Bill number: 6835
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-04-16T08:06:51Z
- Update date including text: 2026-04-16T08:06:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-12 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-12 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6835",
    "number": "6835",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Veterans STAND Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:51Z",
    "updateDateIncludingText": "2026-04-16T08:06:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:07:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T19:39:10Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NJ"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "ME"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NC"
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
      "sponsorshipDate": "2025-12-18",
      "state": "DC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "WI"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "IA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NV"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6835ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6835\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Bergman (for himself, Mr. Bost , Mr. Neguse , Mr. Gottheimer , Mr. Moolenaar , Mr. Golden of Maine , Mr. Huizenga , Mr. Davis of North Carolina , Ms. Norton , Mr. Lawler , Mr. Crow , Ms. Lofgren , Mr. Van Orden , Mr. James , Mr. Nunn of Iowa , and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to offer annual preventative health evaluations to veterans with a spinal cord injury or disorder and increase access to assistive technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Spinal Trauma Access to New Devices Act or the Veterans STAND Act .\n#### 2. Provision of preventative health evaluations for veterans with a spinal cord injury or disorder\nSection 1706 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(d) (1) In managing the provision of hospital care and medical services under section 1710(a) of this title, the Secretary shall furnish (through direct provision of service, referral, or a telehealth program operated by the Department) a preventative health evaluation annually to any veteran with a spinal cord injury or disorder who elects to undergo the evaluation. (2) The evaluation described in paragraph (1) shall include the following: (A) An assessment of any circumstance or condition the veteran is experiencing that indicates a risk for any health complication related to the spinal cord injury or disorder, including a risk of comorbidities. (B) An assessment regarding chronic pain and, if applicable, the management of chronic pain. (C) An assessment regarding dietary management and weight management. (D) An assessment regarding prosthetic equipment, including which prosthetic equipment the veteran needs, how well any existing prosthetic equipment is functioning considering the needs of the veteran, and any safety concerns regarding the prosthetic equipment in use by or recommended to the veteran. (E) An assessment with respect to the provision of assistive technology, including spinal cord neuromodulation technology (such as non-invasive transcutaneous spinal stimulation), that could help maximize the veteran\u2019s voluntary motor or autonomic function, independence, or mobility, including suitability for home use and need for training, programming, and remote follow-up. (3) (A) In maintaining, prescribing, or amending any guidance, rules, or regulations issued by the Department regarding the requirements set out in this subsection, the Secretary shall consult with\u2014 (i) the spinal cord injury and disorder program managers of the Department; (ii) clinicians employed by the Department as specialists in spinal cord injuries and disorders; (iii) clinicians and technologists with demonstrated expertise in spinal cord neuromodulation therapies, including non-invasive transcutaneous approaches; and (iv) representatives of organizations recognzied under section 5902 of this title. (B) Before issuing any guidance, rules, or regulations regarding the requirements set out in this subsection, the Secretary shall consult with manufacturers of assistive technologies and other entities relevant to the provision of assistive technologies if the guidance, rules, or regulations would directly affect such manufacturers or entities. (C) The Secretary shall ensure, to the extent possible, that any veteran known by the Secretary to have a spinal cord injury or disorder receives information annually about the evaluation available under this subsection and the benefits to the veteran of choosing to undergo the evaluation. (4) As the Secretary determines clinically appropriate, the Secretary may provide training, programming, remote monitoring, and follow-up for assistive technologies through telehealth. (5) Not later than one year after the date of the enactment of the Veterans Spinal Trauma Access to New Devices Act, and every two years thereafter, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a report that includes the following: (A) For the period covered by the report\u2014 (i) the number of veterans who\u2014 (I) received medical care or hospital services from the Department and used an assistive technology; (II) received medical care or hospital services from the Department and were assessed for the provision of an assistive technology; and (III) received medical care or hospital services from the Department and were prescribed an assistive technology. (ii) for any assistive technology prescribed, an identification of the category of such technology, including spinal cord neuromodulation, and a summary of functional outcomes associated with the prescription of such technology, if available. (B) The year-to-year change (for the period covered by the report, including the two years immediately prior to year the report is submitted) in the percent of veterans with a spinal cord injury or disorder who received an evaluation under this subsection. (6) In reviewing the performance metrics of a Veterans Integrated Service Network for any year beginning after the date that is one year after the date of the enactment of the Veterans Spinal Trauma Access to New Devices Act, the Secretary shall consider the provision of evaluations under paragraph (1). (7) In this subsection, the term assistive technology means a powered medical device or electronic tool used to treat or alleviate symptoms or conditions caused by a spinal cord injury or disorder, including the following: (A) A personal mobility device, including a powered exoskeleton device. (B) A speech generating device. (C) A spinal cord neuromodulation technology, including non-invasive transcutaneous spinal stimulation using sensory (afferent) pathways, intended to improve voluntary motor function, autonomic function, independence, or quality of life. (D) Where clinically appropriate, and consistent with the prosthetic and sensory aids policies of the Department, an implantable spinal cord stimulation system that is approved by the Food and Drug Administration. .",
      "versionDate": "2025-12-18",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-04",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3988",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans STAND Act",
      "type": "S"
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
        "updateDate": "2026-02-17T18:42:10Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6835ih.xml"
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
      "title": "Veterans STAND Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T06:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans STAND Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T06:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Spinal Trauma Access to New Devices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T06:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to offer annual preventative health evaluations to veterans with a spinal cord injury or disorder and increase access to assistive technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T06:03:27Z"
    }
  ]
}
```
