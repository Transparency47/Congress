# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4027
- Title: Frontline Fighter Force First Act
- Congress: 119
- Bill type: HR
- Bill number: 4027
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-07-21T14:53:21Z
- Update date including text: 2025-07-21T14:53:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-06-24 - IntroReferral: Sponsor introductory remarks on measure. (CR H2899-2900)
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-06-24 - IntroReferral: Sponsor introductory remarks on measure. (CR H2899-2900)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4027",
    "number": "4027",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Frontline Fighter Force First Act",
    "type": "HR",
    "updateDate": "2025-07-21T14:53:21Z",
    "updateDateIncludingText": "2025-07-21T14:53:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2899-2900)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4027ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4027\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Davis of North Carolina (for himself and Mr. Edwards ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo recognize the historical achievements, the ongoing service, and to make a priority recapitalization of the frontline and surge fighter forces at active-duty Air Force bases.\n#### 1. Short title\nThis Act may be cited as the Frontline Fighter Force First Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nEnsuring that the United States military remains the strongest fighting force in the world requires a highly mission capable frontline fighter fleet across fourth, fifth, and next-generation platforms.\n**(2)**\nIn particular, fighter wings that deploy at least 50 percent of the time, including the 335th operational squadron at Seymour Johnson Air Force Base, are on the frontlines of the fight for freedom.\n**(3)**\nAt the same time, with declining mission capable rates, including 55 percent for the F\u201315E fleet, prioritizing recapitalization of legacy aircraft with aging equipment and engines like the Block 220 F\u201315Es must be a priority for the U.S. Air Force. By recapitalizing active-duty bases with upgraded fourth generation aircraft like the F\u201315EX to replace the legacy fleet, the U.S. can fulfill its mission to sustain optimal mission readiness.\n**(4)**\nFurther, that recognizing the historical contributions of Strike Eagle aircraft at a time when they continue to deliver unmatched payload capability and range in active theaters, including CENTCOM, is a high congressional priority.\n**(5)**\nF\u201315E aircraft can carry up to 12 unique missiles, an unrivaled combination of heavy payload and long range with stealth capability.\n**(6)**\nSince their first combat flight, F\u201315Es boast an undefeated 104\u20130 winning record in Air-to-Air missions across the Persian Gulf, Iraqi, and counterterrorism operations in the CENTCOM AOR.\n**(7)**\nDuring the Iraq War, F\u201315E Strike Eagles from Seymour Johnson Air Force Base in Goldsboro, North Carolina, played a significant role, deploying for Operation Iraqi Freedom.\n**(8)**\nThen, on April 13, 2024, with only 24 hours to prepare ahead of an unprecedented ballistic missile attack from Iran, airmen from the 335th operational squadron, under command of the 4th Fighter Wing based at Seymour Johnson deployed in four F\u201315Es that alone intercepted more than two dozen of the one-way attack drones fired at Israel and U.S. military personnel based in the region. They defended our coalition partners, including Israel, embodying the true essence of service.\n**(9)**\nTo commemorate their courage, General Ken Wilsbach, commander of Air Combat Command, awarded airmen from the 4th Fighter Wing high-level decorations during a ceremony at Seymour Johnson Air Force Base. The airmen were recognized for their rapid response and valiant performance in the largest air-to-air engagement in over 50 years. Those heroes, receiving well-deserved decorations and surrounded by their families, have rightfully earned our nation\u2019s deep gratitude. To fighter pilots, maintainers, and all airmen that keep the F\u201315E fleet alive and well, Congress must continue to uplift the power of the E platform, including upgraded F\u201315EX fighters.\n#### 3. Recapitalization of air force active duty frontline fighter force\n##### (a) Procurement of fighter aircraft\n**(1) In general**\nThe Secretary of the Air Force shall take such steps as may be necessary to ensure the continued production and procurement of at least one model of advanced capability fighter aircraft until the date on which the Secretary certifies to the congressional defense committees that the Secretary has replaced all legacy capability fighter aircraft within each Air Combat Command Fighter Wing with an advanced capability fighter aircraft, with replacements made sequentially, starting with fighter squadrons that deploy at least 30 percent of the time.\n**(2) Contracts**\nFor purposes of fulfilling the requirements of paragraph (1), the Secretary shall\u2014\n**(A)**\nseek to enter into a contract for the procurement of advanced capability fighter aircraft; or\n**(B)**\nmodify a contract to provide for the procurement of additional advanced capability fighter aircraft.\n**(3) Gao review and report**\n**(A) Review**\nThe Comptroller General of the United States shall conduct a review of advanced capability fighter aircraft. Such review shall include\u2014\n**(i)**\nan assessment of any challenges to the procurement of such aircraft by the Secretary; and\n**(ii)**\nrecommendations on how to solve such challenges.\n**(B) Briefing**\nNot later than one year after the date of the enactment of this Act, the Comptroller General shall provide to the congressional defense committees a briefing on the preliminary findings of the review conducted under subparagraph (A).\n**(C) Report**\nNot later than 30 days after the Comptroller General provides a briefing under subparagraph (B), the Comptroller General shall submit to the congressional defense committees a final report on the review conducted under subparagraph (A).\n**(4) Report on progress**\nNot later than 180 days after the Comptroller General provides a report under paragraph (3)(C) and on an annual basis thereafter, the Secretary shall submit to the congressional defense committees a report on the progress of the Secretary in\u2014\n**(A)**\nimplementing the recommendations of the Comptroller General issued pursuant to paragraph (3); and\n**(B)**\nreplacing the legacy capability fighter aircraft within each Air Combat Command Fighter Wing with an advanced capability fighter aircraft, fifth generation fighter aircraft, or next-generation air dominance fighter aircraft.\n##### (b) Definitions\nIn this Act:\n**(1)**\nThe term advanced capability fighter aircraft means a Block 70/72 variant or later variant of the F\u201316 fighter aircraft, an F\u201315EX fighter aircraft, an F\u201335 fighter aircraft, an F\u201347 fighter aircraft, any future variant of such fighter aircraft, or any other more advanced capability fighter aircraft identified by the Secretary.\n**(2)**\nThe term congressional defense committees has the meaning given such term in section 101(a)(16) of title 10, United States Code.\n**(3)**\nThe term covered Air Combat Command Fighter Wing means any fighter unit of the Air Force with respect to which the Secretary has not commenced or completed the process of replacing the legacy capability fighter aircraft of such unit with advanced capability fighter aircraft or fifth generation aircraft as of the date of the enactment of this Act.\n**(4)**\nThe term fifth generation has the meaning given such term in section 154(d)(2) of the National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ).\n**(5)**\nThe term fighter aircraft has the meaning given such term in section 9062(i)(2) of title 10, United States Code.\n**(6)**\nThe term legacy capability fighter aircraft has the meaning given such term in section 154(d)(4) of the National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ).",
      "versionDate": "2025-06-17",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-21T14:53:21Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4027ih.xml"
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
      "title": "Frontline Fighter Force First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-28T07:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Frontline Fighter Force First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-28T07:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To recognize the historical achievements, the ongoing service, and to make a priority recapitalization of the frontline and surge fighter forces at active-duty Air Force bases.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-28T07:03:23Z"
    }
  ]
}
```
