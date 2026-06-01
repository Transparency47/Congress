# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8450?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8450
- Title: Save Willy Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8450
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-05-06T22:20:29Z
- Update date including text: 2026-05-06T22:20:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8450",
    "number": "8450",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "L000607",
        "district": "16",
        "firstName": "Sam",
        "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
        "lastName": "Liccardo",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Save Willy Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-06T22:20:29Z",
    "updateDateIncludingText": "2026-05-06T22:20:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "PR"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8450ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8450\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. Liccardo (for himself, Mr. Panetta , Mr. Garamendi , Ms. Lofgren , Mr. Khanna , Mr. Mullin , Mr. Garcia of California , Mr. Hern\u00e1ndez , Mr. Levin , and Mr. Lieu ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require a pilot program to enhance existing efforts to mitigate vessel impacts on large cetaceans in the San Francisco Bay region, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Save Willy Act of 2026 .\n#### 2. Pilot program to enhance efforts to mitigate vessel impacts on large cetaceans in San Francisco Bay region\n##### (a) Establishment\n**(1) In general**\nNot later than one year after the date of the enactment of this section, the Secretary, with the concurrence of the Under Secretary, shall carry out a pilot program to establish a Cetacean Desk, which shall be\u2014\n**(A)**\nlocated and manned within the San Francisco Vessel Traffic Service; and\n**(B)**\ndesigned\u2014\n**(i)**\nto improve coordination with the maritime industry to reduce the risk of vessel impacts on large cetaceans in the San Francisco Bay and the strait of Golden Gate, including impacts from vessel strikes, disturbances, and other sources; and\n**(ii)**\nto monitor the presence and location of large cetaceans in the San Francisco Bay and the strait of Golden Gate.\n**(2) Duration and staffing**\nThe pilot program\u2014\n**(A)**\nshall\u2014\n**(i)**\nbe for a duration of four years; and\n**(ii)**\nrequire not more than two full-time equivalent positions, whose responsibilities shall also include contributing to other necessary San Francisco Vessel Traffic Service duties and responsibilities as needed; and\n**(B)**\nmay be supported by other existing Federal employees, as appropriate.\n##### (b) Engagement with vessel operators\n**(1) In general**\nIn carrying out the pilot program, the Secretary shall require personnel of the Cetacean Desk to engage with vessel operators in areas where large cetaceans have been seen or could reasonably be present to ensure compliance with applicable laws, regulations, and voluntary guidance, to reduce the impact of vessel traffic on large cetaceans.\n**(2) Contents**\nIn engaging with vessel operators as required under paragraph (1), personnel of the Cetacean Desk shall communicate where and when sightings of large cetaceans have occurred.\n##### (c) Memorandum of understanding\nThe Secretary and the Under Secretary may enter into a memorandum of understanding to facilitate real-time sharing of data relating to large cetaceans between the State of California, the National Oceanic and Atmospheric Administration, the San Francisco Vessel Traffic Service, and other relevant entities, as appropriate.\n##### (d) Data\nThe Under Secretary shall leverage existing data collection methods, the program required by section 11303 of the National Defense Authorization Act for Fiscal Year 2023 ( 16 U.S.C. 1391 ), and public data to ensure accurate and timely information on the sighting of large cetaceans.\n##### (e) Use of technologies\n**(1) Emerging technologies**\nThe Secretary, in coordination with the Under Secretary and the Commandant, shall evaluate for potential use under the pilot program, and, as appropriate, adopt for such use, new and emerging technologies to enhance the effectiveness, efficiency, and responsiveness of the Cetacean Desk, including technologies capable of the following:\n**(A)**\nImproving the detection, identification, tracking, or forecasting of large cetacean presence, including through the use of automated, algorithmic, or artificial intelligence-enabled tools.\n**(B)**\nImproving the integration, processing, or dissemination of data from Federal, State, academic, nongovernmental, and public sources in near real time.\n**(C)**\nEnhancing communication with vessel operators to reduce the likelihood of vessel interactions with large cetaceans.\n**(2) Existing partnerships and programs**\nIn carrying out this subsection, the Secretary shall, to the maximum extent practicable, leverage existing research partnerships and other Federal programs.\n##### (f) Consultations\nIn carrying out the pilot program, the Secretary shall consult with Tribal governments, the State of California, institutions of higher education, the maritime industry, ports in the San Francisco Bay region, and nongovernmental organizations.\n##### (g) San Francisco Vessel Traffic Service local variance and policy\nThe Secretary, with the concurrence of the Under Secretary and in consultation with the Captain of the Port for the San Francisco Bay\u2014\n**(1)**\nshall implement local variances, as authorized by section 70001(c) of title 46, United States Code, to facilitate communication, reporting, and voluntary coordination between vessel operators and the San Francisco Vessel Traffic Service regarding the presence of large cetaceans;\n**(2)**\nshall ensure that any local variances implemented under this subsection maintain safe vessel navigation and are consistent with the communication and coordination functions of the San Francisco Vessel Traffic Service; and\n**(3)**\nmay enter into cooperative agreements, in accordance with section 70001(d) of title 46, United States Code, with Federal, State, Tribal, and local officials to reduce the likelihood of vessel interactions with protected large cetaceans, which may include\u2014\n**(A)**\ncommunicating marine mammal protection guidance to vessels;\n**(B)**\ntraining on requirements imposed by local, State, Tribal, and Federal laws and regulations and guidelines concerning\u2014\n**(i)**\nvessel buffer zones;\n**(ii)**\nvessel speed;\n**(iii)**\nseasonal no-go zones for vessels;\n**(iv)**\nprotected areas, including areas designated as critical habitat, as applicable to marine operations; and\n**(v)**\nany other activities to reduce the direct and indirect impact of vessel traffic on large cetaceans;\n**(C)**\ntraining to understand, utilize, and communicate large cetacean location data; and\n**(D)**\ntraining to understand and communicate basic large cetacean detection, identification, and behavior, including\u2014\n**(i)**\ncues of the presence of large cetaceans such as spouts, water disturbances, breaches, or presence of prey;\n**(ii)**\nimportant feeding, breeding, calving, and rearing habitats that co-occur with areas of high risk of vessel strikes;\n**(iii)**\nseasonal large cetacean migration routes that co-occur with areas of high risk of vessel strikes; and\n**(iv)**\nareas designated as critical habitat for large cetaceans.\n##### (h) Reports required\nNot later than one year after the date of enactment of this section, and annually thereafter for the duration of the pilot program, the Commandant, in coordination with the Under Secretary and the Administrator of the Maritime Administration, shall submit to the appropriate congressional committees a report that\u2014\n**(1)**\nevaluates the functionality, utility, reliability, responsiveness, and operational status of the Cetacean Desk, including a quantification of reductions in vessel strikes to large cetaceans as a result of the pilot program;\n**(2)**\nassesses the efficacy of communication between the Cetacean Desk and the maritime industry and provides recommendations for improvements;\n**(3)**\nevaluates the integration and interoperability of existing data collection methods, as well as public data, into the Cetacean Desk operations;\n**(4)**\nassesses the efficacy of collaboration and stakeholder engagement with Tribal governments, the State of California, institutions of higher education, the maritime industry, ports in the San Francisco Bay region, and nongovernmental organizations; and\n**(5)**\nevaluates the progress, performance, and implementation of guidance and training procedures for San Francisco Vessel Traffic Service personnel, as required under subsection (f).\n##### (i) Definitions\nIn this section:\n**(1)**\nThe terms appropriate congressional committees , institution of higher education , Tribal government , and Under Secretary have the meanings given those terms in section 11301 of the National Defense Authorization Act for Fiscal Year 2023 ( Public Law 117\u2013263 ; 16 U.S.C. 1390 note).\n**(2)**\nThe term Cetacean Desk means the Cetacean Desk established by the pilot program.\n**(3)**\nThe term Commandant means the Commandant of the Coast Guard.\n**(4)**\nThe term large cetacean means all species within\u2014\n**(A)**\nthe suborder Mysticeti;\n**(B)**\nthe genera Physeter; or\n**(C)**\nthe genera Orcinus.\n**(5)**\nThe term pilot program means the pilot program required under subsection (a).\n**(6)**\nThe term Secretary means the Secretary of the department in which the Coast Guard is operating.",
      "versionDate": "2026-04-22",
      "versionType": "Introduced in House"
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
        "name": "Animals",
        "updateDate": "2026-05-06T22:20:29Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8450ih.xml"
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
      "title": "Save Willy Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save Willy Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a pilot program to enhance existing efforts to mitigate vessel impacts on large cetaceans in the San Francisco Bay region, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:49Z"
    }
  ]
}
```
