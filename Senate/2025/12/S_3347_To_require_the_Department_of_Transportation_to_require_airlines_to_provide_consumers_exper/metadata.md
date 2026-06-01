# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3347?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3347
- Title: Flight Delay and Cancellation Compensation Act
- Congress: 119
- Bill type: S
- Bill number: 3347
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-01-07T16:18:48Z
- Update date including text: 2026-01-07T16:18:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3347",
    "number": "3347",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Flight Delay and Cancellation Compensation Act",
    "type": "S",
    "updateDate": "2026-01-07T16:18:48Z",
    "updateDateIncludingText": "2026-01-07T16:18:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T18:31:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "AZ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "VT"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MD"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "RI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MD"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CO"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "OR"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "PA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "IL"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "RI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "MN"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-04",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3347is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3347\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Kelly (for himself, Mr. Blumenthal , Mr. Markey , Mr. Gallego , Ms. Smith , Mr. Welch , Ms. Alsobrooks , Mr. Reed , Mr. Van Hollen , Mr. Bennet , Mr. Wyden , Mr. Fetterman , Ms. Duckworth , Mr. Whitehouse , Ms. Klobuchar , Mr. Sanders , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Department of Transportation to require airlines to provide consumers experiencing significant flight disruptions or cancellations cash compensation, free rebooking, and reimbursement for amenities, such as meals, lodging for overnight delays, and transportation to and from lodging.\n#### 1. Short title\nThis Act may be cited as the Flight Delay and Cancellation Compensation Act .\n#### 2. Flight Delay and Cancellation Compensation\n##### (a) Aviation rulemaking committee\n**(1) In general**\nNot later than 90 days after the date of enactment of this section, the Administrator shall establish an Aviation Rulemaking Committee (in this section referred to as the Committee ) to review and develop recommendations regarding the following:\n**(A)**\nImplementation of the requirements of section 512 of the FAA Reauthorization Act of 2024 (49 U.S.C. note prec. 42301), as amended by subsection (e) of this section.\n**(B)**\nEnsuring that air carriers and foreign air carriers provide passengers with the following when a flight operated by such air carrier or a foreign air carrier is cancelled or significantly delayed and such cancellation or delay is directly attributable to such air carrier or foreign air carrier:\n**(i)**\nCash compensation of\u2014\n**(I)**\nat least $300 for a delay of more than 3 hours but less than 6 hours; and\n**(II)**\nat least $600 for a delay of 6 hours or more.\n**(ii)**\nFree rebooking.\n**(2) Composition**\nThe Committee shall consist of members appointed by the Administrator, including the following:\n**(A)**\nAir carriers and foreign air carriers.\n**(B)**\nAirport operators.\n**(C)**\nRepresentatives of consumer protection organizations.\n**(D)**\nRepresentatives of the Office of the Secretary of the Department of Transportation.\n**(E)**\nRepresentatives of the Federal Trade Commission.\n**(3) Report to the Administrator and the Secretary**\nNot later than 12 months after the date of enactment of this section, the Committee shall submit to the Administrator and the Secretary a report detailing the consensus findings and recommendations of the Committee. Such report shall include recommendations regarding each of the following:\n**(A)**\nA requirement that air carriers and foreign air carriers provide cash compensation to passengers impacted by cancelled or significantly delayed flights comparable to\u2014\n**(i)**\nthe Canadian Transportation Agency (CTA) Air Passenger Protection Regulations, including a requirement that the minimum cash compensation is $300 for a delay of more than 3 hours but less than 6 hours and $600 for a delay of 6 hours or more; and\n**(ii)**\nregulation (EC) No 261/2004 of the European Parliament and of the Council.\n**(B)**\nA plan to implement the requirements of Article 19 of the Convention for the Unification of Certain Rules for International Carriage by Air (Montreal Convention).\n**(C)**\nA requirement that air carriers and foreign air carriers cover the costs of amenities, such as meals, lodging for overnight delays, and transportation to and from lodging, when a flight is cancelled or significantly delayed.\n**(D)**\nA process for determining whether a cancelled or significantly delayed flight is directly attributable to such air carrier or foreign air carrier.\n**(E)**\nThe development of an educational process to ensure that passengers receive the correct information from the air carrier or foreign air carrier in a timely manner regarding the compensation and reimbursement options they are eligible to receive in the case of cancelled or significantly delayed flights.\n**(F)**\nHow to ensure that the process for passengers to receive cash compensation and reimbursement for amenities for cancelled or significantly delayed flights is clear, simple, straightforward, and prompt.\n**(G)**\nHow to ensure that the process for passengers to receive cash compensation from an air carrier or foreign air carrier for provable direct or consequential damages resulting from the disappearance of, damage to, or delay in delivery of a passenger's personal property, including baggage, is clear, simple, straightforward, and prompt.\n**(H)**\nOther recommendations determined appropriate by the Committee.\n##### (b) Rulemaking\n**(1) Notice of proposed rulemaking**\nNot later than 90 days after the date on which the Committee submits the report under subsection (a)(3), the Secretary, taking into account the recommendations of the Committee included in such report, shall issue a notice of proposed rulemaking to implement\u2014\n**(A)**\nthe requirements of section 512 of the FAA Reauthorization Act of 2024 (49 U.S.C. note prec. 42301), as amended by subsection (e) of this section;\n**(B)**\nthe matter described in subsection (a)(1)(B) of this section; and\n**(C)**\nother recommendations of the Committee as determined appropriate by the Secretary.\n**(2) Application of interim final rule until effective date of final rule**\n**(A) In general**\nNot later than 18 months after the date of enactment of this Act, the Secretary shall promulgate an interim final rule that, at a minimum, includes the following requirements when a flight operated by an air carrier or a foreign air carrier is cancelled or significantly delayed:\n**(i)**\nThe air carrier or foreign air carrier shall provide $750 in cash compensation to any passenger impacted by such cancellation or delay if such cancellation or delay is directly attributable to such air carrier or foreign air carrier.\n**(ii)**\nThe air carrier or foreign air carrier shall find a seat on another flight offered by the same air carrier or foreign air carrier or another air carrier or foreign air carrier or on an alternative means of transportation at no additional cost to the passenger, at the earliest available opportunity, if the passenger so chooses, for any passenger impacted by cancellation or delay if such cancellation or delay is directly attributable to such air carrier or foreign air carrier.\n**(iii)**\nThe air carrier or foreign air carrier shall provide a meal or meal credit to any passenger impacted by such cancellation or delay.\n**(iv)**\nIn the case of a passenger affected by an overnight flight cancellation or significantly delayed flight, the air carrier or foreign air carrier shall provide the passenger with\u2014\n**(I)**\neach of the requirements described in clauses (i), (ii), and (iii);\n**(II)**\ncomplimentary hotel accommodations or reimbursement for lodging costs; and\n**(III)**\ncomplimentary ground transportation to and from the hotel.\n**(B) Application**\nThe interim final rule promulgated under subparagraph (A) shall be effective during the period beginning on the date that is 2 years after the date of enactment of this section and ending on the effective date of the final rule described in paragraph (1).\n##### (c) Reports to Congress\nNot later than 6 months after the date of enactment of this section, and every 6 months thereafter until the Secretary promulgates a final rule under subsection (b), the Secretary shall submit to the appropriate committees of Congress a report on the status of the rulemaking under paragraphs (1) and (2) of subsection (b), including the development of the requirements for air carriers and foreign air carriers.\n##### (d) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Aviation Administration.\n**(2) Air carrier**\nThe term air carrier has the meaning given such term in section 40102(a) of title 49, United States Code.\n**(3) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(B)**\nthe Committee on Appropriations of the Senate;\n**(C)**\nthe Committee on Transportation and Infrastructure of the House of Representatives; and\n**(D)**\nthe Committee on Appropriations of the House of Representatives.\n**(4) Foreign air carrier**\nThe term foreign air carrier has the meaning given such term in section 40102(a) of title 49, United States Code.\n**(5) Significantly delayed**\nThe term significantly delayed has the meaning given such term in section 512 of the FAA Reauthorization Act of 2024 (49 U.S.C. note prec. 42301).\n**(6) Secretary**\nThe term Secretary means the Secretary of Transportation.\n##### (e) Conforming amendment\nSection 512 of the FAA Reauthorization Act of 2024 (49 U.S.C. note prec. 42301) is amended by striking subsection (c).\n##### (f) Clarification\nFor the purposes of implementing this section and such section 512, the term air carrier under such section 512 is deemed to include foreign air carriers.",
      "versionDate": "2025-12-04",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-07T16:18:48Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3347is.xml"
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
      "title": "Flight Delay and Cancellation Compensation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Flight Delay and Cancellation Compensation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Department of Transportation to require airlines to provide consumers experiencing significant flight disruptions or cancellations cash compensation, free rebooking, and reimbursement for amenities, such as meals, lodging for overnight delays, and transportation to and from lodging.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:25Z"
    }
  ]
}
```
