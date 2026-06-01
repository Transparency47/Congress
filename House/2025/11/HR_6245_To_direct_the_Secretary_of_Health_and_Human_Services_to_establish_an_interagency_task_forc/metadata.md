# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6245?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6245
- Title: PLAY Act
- Congress: 119
- Bill type: HR
- Bill number: 6245
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-01-22T15:19:18Z
- Update date including text: 2026-01-22T15:19:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6245",
    "number": "6245",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "PLAY Act",
    "type": "HR",
    "updateDate": "2026-01-22T15:19:18Z",
    "updateDateIncludingText": "2026-01-22T15:19:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "NE"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6245ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6245\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Williams of Georgia (for herself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to establish an interagency task force on youth health and wellness to encourage community-supported physical activity spaces.\n#### 1. Short title\nThis Act may be cited as the Prioritizing Lifestyle and Activity for Youth Act or the PLAY Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPlaygrounds help enhance children\u2019s cognitive functions and build important creative thinking and problem-solving skills that contributes to their emotional and physical well-being.\n**(2)**\nPlaygrounds are critical to children\u2019s physical and mental health, and every child in America deserves access to a safe and quality place to play.\n**(3)**\nLocal green spaces can reduce surface heat temperatures by 10 to 20 degrees, which has become the number one weather-related killer in the United States.\n**(4)**\nSafe and accessible playgrounds are proven public health infrastructure that promote physical activity, reduce chronic disease risk, support social-emotional development, and strengthen community cohesion.\n#### 3. Interagency Task Force on Child Wellness and Physical Activity Infrastructure\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Health and Human Services shall establish a task force to be known as the Task Force on Child Wellness and Physical Activity Infrastructure (in this section referred to as the Task Force ).\n##### (b) Composition\nThe Task Force shall be composed of the following members or their designees:\n**(1)**\nThe Secretary of Health and Human Services.\n**(2)**\nThe Secretary of the Interior.\n**(3)**\nThe Administrator of the Environmental Protection Agency.\n**(4)**\nThe Secretary of Agriculture.\n**(5)**\nThe Secretary of Housing and Urban Development.\n**(6)**\nThe Secretary of Transportation.\n**(7)**\nThe Chair of the Council on Environmental Quality.\n**(8)**\nThe Secretary of Defense.\n**(9)**\nThe Chief of the Army Corps of Engineers.\n**(10)**\nThe Chief Executive Officer of the Corporation for National and Community Service.\n**(11)**\nThe Secretary of Education.\n**(12)**\nAny other member that the Secretary of Health and Human Services determines to be appropriate.\n##### (c) Chairpersons\nThe Secretary of Health and Human Services and the Secretary of the Interior shall serve as co-chairpersons of the Task Force (in this section referred to as the Chairpersons ).\n##### (d) Duties\n**(1) Task force**\nThe duties of the Task Force shall be\u2014\n**(A)**\nto identify opportunities to formalize coordination between the Department of Health and Human Services, public health and public lands agencies, and partner organizations regarding the use of outdoor spaces for creating outdoor environments that encourage physical activity and well-being among youth;\n**(B)**\nto identify existing barriers to providing children with opportunities for accessing close-to-home, community-driven, and outdoor spaces;\n**(C)**\nto develop recommendations to better facilitate active play for the promotion of health and well-being, academic learning, and safe community centers;\n**(D)**\nto develop recommendations for how agencies may work together to ensure the ability of child wellness infrastructure to meet the diverse health, environmental, and resiliency needs of the surrounding community; and\n**(E)**\nto identify and promote scalable models, such as public-private partnerships between public, private, and nonprofit sector organizations, that build evidence-based play environments proven to improve children\u2019s physical and emotional health.\n**(2) Consultation**\nThe Task Force shall carry out the duties under paragraph (1) in consultation with appropriate health and wellness and outdoor recreation groups, including organizations with experience in community-led playground development, child health, and physical activity promotion.\n##### (e) Reports\n**(1) Preliminary report**\nNot later than 180 days after the date on which the Task Force is established, the Chairpersons shall submit to the appropriate congressional committees a report on the preliminary findings of the Task Force.\n**(2) Final report**\nNot later than one year after the date of the submittal of the preliminary report under paragraph (1), the Chairpersons shall submit to the appropriate congressional committees a report on the findings of the Task Force, which shall include the recommendations developed under subparagraphs (C) and (D) of subsection (d)(1).\n##### (f) Duration\nThe Task Force shall terminate on the date that is one year after the date of the submittal of the final report under subsection (e)(2).\n##### (g) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Commerce of the House of Representatives; and\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate.\n**(2) Child wellness infrastructure**\nThe term child wellness infrastructure means community-based environments intentionally designed to support children\u2019s physical activity, play, and health. Such infrastructure may include playgrounds, outdoor learning spaces, nature play areas, and safe places for movement and social interaction.\n**(3) Public lands**\nThe term public lands means any lands under the jurisdiction of the Federal Government or a State or local government.\n**(4) Youth**\nThe term youth means any individual under the age of 18.",
      "versionDate": "2025-11-20",
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
        "name": "Health",
        "updateDate": "2026-01-22T15:19:18Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6245ih.xml"
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
      "title": "PLAY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PLAY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prioritizing Lifestyle and Activity for Youth Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to establish an interagency task force on youth health and wellness to encourage community-supported physical activity spaces.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:33:42Z"
    }
  ]
}
```
