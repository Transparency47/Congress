# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6874?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6874
- Title: Roadway Safety Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6874
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-03-04T09:06:36Z
- Update date including text: 2026-03-04T09:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6874",
    "number": "6874",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000871",
        "district": "1",
        "firstName": "Tracey",
        "fullName": "Rep. Mann, Tracey [R-KS-1]",
        "lastName": "Mann",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Roadway Safety Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-04T09:06:36Z",
    "updateDateIncludingText": "2026-03-04T09:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:44:06Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
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
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "KS"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "CA"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "AR"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6874ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6874\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Mann (for himself and Ms. Davids of Kansas ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to allow recipients of certain grants to improve highway safety efforts through the integration of predictive data analytics, telematics, and other advanced technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Roadway Safety Modernization Act of 2025 .\n#### 2. Inclusion of highway safety technology in certain highway and freight safety programs\n##### (a) Amendments to highway safety programs\n**(1) Highway safety improvement program**\nSection 148 of title 23, United States Code, is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (4)(B) by adding at the end the following new clause:\n(xxx) The development, acquisition, or deployment of safety data and systems, including predictive analytics, telematics, and other validated methodology tools for purposes of highway safety. ;\n**(ii)**\nin paragraph (10)(B) by striking includes, and all that follows through the period at the end and inserting\nincludes\u2014 (i) in the case of a railway-highway grade crossing, the characteristics of highway and train traffic, licensing, and vehicle data; and (ii) to the extent practicable, data collected via predictive analytics, telematics, or other validated methodology tools for use in risk modeling and highway safety planning. ; and\n**(iii)**\nin paragraph (13)\u2014\n**(I)**\nby redesignating subparagraphs (H) through (J) as subparagraphs (I) through (K), respectively; and\n**(II)**\nby inserting after subparagraph (G) the following:\n(H) incorporates predictive analytics, telematics, or other validated methodology tools for use in risk modeling and highway safety planning; ; and\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (1)(B) by striking ; and and inserting , including by using of safety data to proactively identify and address roadway safety risks and such safety problems; and ;\n**(ii)**\nin paragraph (2)(A)\u2014\n**(I)**\nin clause (v) by striking and at the end;\n**(II)**\nin clause (vi) by striking the semicolon and inserting ; and ; and\n**(III)**\nby adding at the end the following new clause:\n(vii) using crash data and predictive analytics, telematics, or other validated methodology tools; ; and\n**(iii)**\nin paragraph (2)(B)\u2014\n**(I)**\nin clause (iv) by striking and at the end; and\n**(II)**\nby adding at the end the following new clauses:\n(vi) evaluate how effective a safety project is at reducing crashes, injuries, or fatalities; and (vii) assess the comparative benefits, if any, of safety strategies and interventions to determine which such strategies and interventions yield the greatest improvement to safety, taking into account characteristics of various locations and risk factors; .\n**(2) National highway freight program**\nSection 167 of title 23, United States Code, is amended\u2014\n**(A)**\nin subsection (h)\u2014\n**(i)**\nin paragraph (5)(C) by adding at the end the following new clause:\n(xxiv) Development, acquisition, or deployment of safety data tools, including predictive analytics, telematics, and other validated methodology tools to improve freight safety and support performance-based planning, including performance-based planning under sections 134 and 135. ; and\n**(ii)**\nin paragraph (6)(B)(i) by inserting before the semicolon , including the use of predictive analytics, telematics, and other validated methodology tools ;\n**(B)**\nin subsection (j), by amending to read as follows:\n(j) Intelligent freight transportation system operating standards Not later than 1 year after the date of enactment of the Roadway Safety Modernization Act of 2025 , the Administrator shall\u2014 (1) determine whether there is a need for establishing operating standards for intelligent freight transportation systems; and (2) if the Administrator determines there is such a need, submit to Congress a report on such need. ; and\n**(C)**\nby adding at the end the following new subsection:\n(l) Definitions In this section: (1) Intelligent freight transportation system The term intelligent freight transportation system means\u2014 (A) innovative or intelligent technological transportation systems, infrastructure, or facilities, including elevated freight transportation facilities\u2014 (i) in proximity to, or within, an existing right of way on a Federal-aid highway; or (ii) that connect land ports of entry to existing Federal-aid highways; or (B) communications or information processing systems that improve the efficiency, security, or safety of freight movements on the Federal-aid highway system, including to improve the conveyance of freight on dedicated intelligent freight lanes. (2) Safety data The term safety data has the meaning given such term in section 148(a). .\n**(3) National priority safety programs**\nSection 405(c) of title 23, United States Code, is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (E) by striking the period at the end and inserting ; and ; and\n**(ii)**\nby adding at the end the following:\n(F) encourage the integration of predictive analytics, telematics, and other validated methodology tools into safety data systems of the State. ; and\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (H)(ii) by striking and at the end;\n**(ii)**\nin subparagraph (I) by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(J) deploying or using predictive analytics, telematics, and other validated methodology tools to identify high-risk roadway segments, evaluate crash causation factors, and support the development of performance-based planning, including performance-based planning under sections 134 and 135. .\n##### (b) Guidance\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation shall develop and issue guidance regarding best practices for\u2014\n**(1)**\nanonymizing data collected for highway safety purposes, securing such data, and protecting personally identifiable information;\n**(2)**\npromoting transparency and accountability in using predictive analytics, telematics, and other validated methodology tools; and\n**(3)**\nensuring that safety data and related technologies are grounded in validated methodologies (such as actuarial validation, behavioral risk analysis, and other proven risk indicators) to ensure, to the extent practicable, the reliability and effectiveness of such data and technologies.\n##### (c) Coordination; consultation\nThe Secretary shall\u2014\n**(1)**\nwithin the Department of Transportation, ensure the coordination of activities carried out with respect to, or programs that fund the use of, predictive safety tools, including any such activities or programs of the Federal Highway Administration, National Highway Traffic Safety Administration, Federal Motor Carrier Safety Administration, Federal Railroad Administration, Office of the Assistant Secretary for Research and Technology, and the Intelligent Transportation Systems Joint Program Office; and\n**(2)**\nconsult with the Secretary of Energy, the Secretary of Commerce, and the heads of any other agency determined appropriate by the Secretary of Transportation to promote the effective use of predictive analytics, telematics, and other validated methodology tools in, and ensure interoperability of such tools across, Federal programs.",
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
        "actionDate": "2025-12-18",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3572",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Roadway Safety Modernization Act of 2025",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-26T13:15:01Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6874ih.xml"
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
      "title": "Roadway Safety Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Roadway Safety Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to allow recipients of certain grants to improve highway safety efforts through the integration of predictive data analytics, telematics, and other advanced technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T03:33:17Z"
    }
  ]
}
```
