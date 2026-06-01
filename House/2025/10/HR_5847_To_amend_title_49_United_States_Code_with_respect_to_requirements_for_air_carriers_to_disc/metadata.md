# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5847?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5847
- Title: Airline Travelers Right to Know Act
- Congress: 119
- Bill type: HR
- Bill number: 5847
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2026-01-07T09:05:58Z
- Update date including text: 2026-01-07T09:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-29 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-29 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5847",
    "number": "5847",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Airline Travelers Right to Know Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:58Z",
    "updateDateIncludingText": "2026-01-07T09:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
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
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-10-29T17:02:31Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5847ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5847\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Mr. Espaillat introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, with respect to requirements for air carriers to disclose certain exposures to toxic fumes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Airline Travelers Right to Know Act .\n#### 2. Airline toxic fume disclosure\n##### (a) In general\nSubpart III of part A of subtitle VII of title 49, United States Code, is amended by adding at the end the following:\n455 Toxic Fume Disclosure Sec. 45401. Definition of Administrator. Sec. 45402. Toxic fume disclosure. Sec. 45403. Passenger notification prior to ticket purchase and check-in. Sec. 45404. Immediate notification of toxic fume events aboard aircraft. Sec. 45405. Crew notification of toxic fume events. 45401. Definition of Administrator In this chapter, the term Administrator means the Administrator of the Federal Aviation Administration. 45402. Toxic fume disclosure (a) In general Not later than 180 days after the date of enactment of this section, the Administrator shall implement and enforce a right to know of potential toxic fume exposure policy to inform air carrier passengers, pilots, and cabin crew employees of the potential exposure to toxic fumes that cause permanent health or brain damage that such passengers, pilots, or employees may encounter onboard passenger-carrying aircraft operating under part 121 of title 14, Code of Federal Regulations. (b) Requirements The right to know of potential toxic fume exposure policy under subsection (a) shall\u2014 (1) be made available in all pilot and crew member contracts; (2) be made available to all air carrier passengers immediately after purchasing a ticket for transportation by such air carrier or a third party ticket booking entity; (3) include details on the potential for acute or chronic impairment relating to such fumes to an individual; (4) include details on chemicals known to cause cancer, birth defects, and other reproductive harm that may be present in jet engine exhaust, fumes from jet fuel, and exhaust from equipment used to service airplanes, while making clear that sometimes such chemicals enter the jet bridge and are present throughout the duration of the flight; (5) provide information on safety management systems in place that could protect individuals from such exposure; (6) provide information on safety management systems to use if exposed to toxic fumes such as oxygen therapy; and (7) provide that passengers of air carriers and air carrier crew members have a right to use cabin oxygen masks in response to a toxic fume event. (c) Civil penalty The Administrator shall impose a civil penalty under section 46301 for each violation of the disclosure required pursuant to subsection (a). 45403. Passenger notification prior to ticket purchase and check-in Beginning on the date of enactment of this section, operators of passenger-carrying aircraft operating under part 121 of title 14, Code of Federal Regulations, shall require passengers to indicate an understanding of potential toxic fume exposure onboard such aircraft in ticket purchase process. 45404. Immediate notification of toxic fume events aboard aircraft Beginning on the date of enactment of this section, the Administrator shall notify all affected customers, flight attendants, pilots, and aircraft maintenance technicians of any exposure to toxic fumes aboard aircraft as soon as an air carrier confirms to the Administrator toxic fumes were detected onboard such aircraft. 45405. Crew notification of toxic fume events (a) In general Operators of passenger-carrying aircraft under part 121 of title 14, Code of Federal Regulations, shall inform all crewmembers of such aircraft of the most recent toxic fume exposure on such aircraft, whether the issue that led to the exposure has been resolved, and if any crewmembers have requested treatment for such exposure. (b) Right To decline assignment Operators under subsection (a) shall provide crewmembers with an option to decline an assignment onboard an aircraft covered under subsection (a) if the issue that led to an exposure reported under such subsection has not been resolved, without penalizing such crewmember. 45406. Civil penalty for false statement, misrepresentation, imparting, or conveying false information (a) In general The Administrator shall impose a civil penalty under section 46301 for each specified violation. (b) Specified violation In this section, the term specified violation means any false statement, misrepresentation, impart, or conveyance of false information by an operator of an aircraft under section 45404 or 45405 demonstrated by a confirmed illness of a customer or employee of a flight provided by such operator. 45407. Penalty for missing reports If an operator of passenger-carrying aircraft under part 121 of title 14, Code of Federal Regulations, that is required to report information under this chapter is missing any such report on inspection by the Secretary of Transportation, the operator shall be liable to the United States Government for a civil penalty of $100,000. .\n##### (b) Clerical amendment\nThe analysis for subtitle VII of title 49, United States Code, is amended by inserting after the item relating to chapter 453 the following:\n455. Toxic Fume Disclosure .\n##### (c) Regulation\nThe Administrator of the Federal Aviation administration shall issue such regulations as are necessary to amend section 13.18 of title 14, Code of Federal Regulations, to include violations under section 45402 of title 49, United States Code, under the procedures for civil penalties under such section 13.18.\n##### (d) Toxic fume sensors\nNot later than 15 days after the date of enactment of this Act, the Secretary of Transportation shall issue such regulations as are necessary to\u2014\n**(1)**\nrequire operators of passenger-carrying aircraft under part 121 of title 14, Code of Federal Regulations, to install sensors that detect toxic fumes onboard such aircraft; and\n**(2)**\namend section 13.18 of title 14, Code of Federal Regulations, to include violations of the regulations issued under paragraph (1) under the procedures for civil penalties under such section 13.18.\n##### (e) Oxygen for crewmembers\nNot later than 15 days after the date of enactment of this Act, the Secretary of Transportation shall issue such regulations as are necessary to require operators of passenger-carrying aircraft under part 121 of title 14, Code of Federal Regulations, to procure and make available to all crewmembers on such aircraft mobile oxygen masks for crewmembers assisting passengers with oxygen masks in the case of a toxic fume event.",
      "versionDate": "2025-10-28",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-02T16:50:12Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5847ih.xml"
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
      "title": "Airline Travelers Right to Know Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T03:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Airline Travelers Right to Know Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T03:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, with respect to requirements for air carriers to disclose certain exposures to toxic fumes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T03:48:16Z"
    }
  ]
}
```
