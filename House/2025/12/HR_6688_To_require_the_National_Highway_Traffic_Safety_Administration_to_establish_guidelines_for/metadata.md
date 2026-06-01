# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6688?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6688
- Title: ADAS Functionality and Integrity Act
- Congress: 119
- Bill type: HR
- Bill number: 6688
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-04-13T19:07:53Z
- Update date including text: 2026-04-13T19:07:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-12 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-12 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6688",
    "number": "6688",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "ADAS Functionality and Integrity Act",
    "type": "HR",
    "updateDate": "2026-04-13T19:07:53Z",
    "updateDateIncludingText": "2026-04-13T19:07:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-12",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-10T20:54:46Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-10T20:54:27Z",
                "name": "Markup by"
              },
              {
                "date": "2025-12-12T20:54:13Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "CA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "NM"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6688ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6688\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Mrs. Harshbarger (for herself, Mr. Obernolte , Mr. Vasquez , and Mrs. Torres of California ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the National Highway Traffic Safety Administration to establish guidelines for advanced driver assistance systems calibration, modifications, and tolerances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ADAS Functionality and Integrity Act .\n#### 2. ADAS modification ranges and tolerances guidelines\n##### (a) Guidelines for ADAS\nNot later than 24 months after the date of the enactment of this Act, the Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration, in consultation with manufacturers of passenger motor vehicles and equipment, standard settings organizations, the independent automotive aftermarket, and dealers, shall develop and publish guidelines to ensure ADAS and vehicle dynamic systems installed in any passenger motor vehicle, for a model year on and after 2028 maintains functionality when a passenger motor vehicle is modified or customized that include the following:\n**(1)**\nAllowable modification ranges and tolerances, including physical parameters impacting ADAS and vehicle dynamic systems functionality, including ride height, wheel and tire dimensions, overall static geometry, physical displacement parameters, and sensor and camera function.\n**(2)**\nA process for manufacturers to provide vehicle tolerance and system sensitivity information relevant to modification and calibration to owners and the Administrator within 30 days after the release of a passenger motor vehicle.\n**(3)**\nQuantifiable tolerance thresholds for changes in vertical and lateral displacement, in all axes, necessary to maintain proper ADAS functionality.\n**(4)**\nProper calibration procedures of ADAS and other vehicle dynamic systems following repair, modification, or component replacement.\n**(5)**\nConfirmatory test protocols and performance validation metrics that allow owners, service providers, and independent repair facilities to verify the operational integrity of ADAS after calibration.\n##### (b) Contracting authority\nThe Administrator may contract with independent laboratories and vehicle testing facilities to carry out any testing that may be required to develop the guidelines under subsection (a).\n##### (c) Requirement To use empirical data\nAny determination made by the Administrator in issuing the guidelines required pursuant to subsection (a) shall be based on empirical data derived from dynamic testing, independent research, and public data sources.\n##### (d) Use of NCAP methodologies\nThe guidelines described in subsection (a)(4) shall reference or expand upon methodologies established by the United States New Car Assessment Program, including\u2014\n**(1)**\na standardized scoring scale to evaluate the effectiveness of calibration (such as good, fair, and poor); and\n**(2)**\ntransparent validation criteria that can be applied across vehicle platforms and assessed over the lifecycle of the vehicle.\n##### (e) Enforcement\nA manufacturer of a passenger motor vehicle or equipment that does not meet the guidelines issued pursuant to this section is subject to the civil penalties described under section 30165(a) of title 49, United States Code.\n#### 3. ADAS modification ranges and tolerances study\n##### (a) Study required\nNot later than 12 months after the date of the enactment of this Act, the Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration, shall complete a study and submit to Congress a report that assesses the safety needs, feasibility, capability, and cost to the National Highway Traffic Safety Administration to develop and maintain industry guidelines to support the functionality of ADAS and vehicle dynamic systems installed in passenger motor vehicles for a model year on and after 2028 after a passenger motor vehicle is modified or customized. The study shall consider the development of industry guidelines relating to the following:\n**(1)**\nVehicle tolerance and system sensitivity information relevant to calibration following modification.\n**(2)**\nAllowable modification ranges and tolerances for passenger motor vehicles, including physical parameters that impact ADAS and vehicle dynamic systems functionality, including ride height, wheel and tire dimensions, overall static geometry, physical displacement parameters, and sensor and camera function.\n**(3)**\nQuantifiable tolerance thresholds for changes in vertical, longitudinal, and lateral displacement, in all axes, necessary to maintain proper ADAS functionality.\n**(4)**\nProper calibration procedures of ADAS and other vehicle dynamic systems following repair, modification, or component replacement.\n**(5)**\nConfirmatory test protocols and performance validation metrics that allow owners, service providers, and independent repair facilities to verify the operational integrity of ADAS after calibration.\n##### (b) Stakeholder outreach\nIn carrying out the study required under subsection (a), the Administrator shall consult with manufacturers of passenger motor vehicles and equipment, standard setting organizations, the independent automotive aftermarket, and dealers.\n#### 4. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the National Highway Traffic Safety Administration.\n**(2) Advanced driver assistance systems; ADAS**\nThe term advanced driver assistance system or ADAS means a passenger motor vehicle equipped with a Level 0, Level 1 or Level 2 system.\n**(3) Dealer; manufacturer**\nThe terms dealer and manufacturer have the meaning given those terms in section 30102 of title 49, United States Code.\n**(4) Confirmatory test**\nThe term confirmatory test means a standardized post-calibration vehicle test designed to validate system performance.\n**(5) Independent automotive aftermarket**\nThe term independent automotive aftermarket means any party or entity not authorized by a passenger motor vehicle manufacturer or affiliated service provider.\n**(6) Level 0; Level 1; Level 2**\nThe terms Level 0 , Level 1 , and Level 2 have the meaning given those terms in the April 2021 edition of the J3016 recommended practice of SAE International, Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles , or any subsequent edition of J3016 adopted by the Secretary.\n**(7) Motor vehicle**\nThe term motor vehicle has the meaning given that term in section 32101 of title 49, United States Code.\n**(8) Owner**\nThe term owner has the meaning given that term in section 30106(d)(2) of title 49, United States Code.\n**(9) Passenger motor vehicle**\nThe term passenger motor vehicle has the meaning given that term in section 32101 of title 49, United States Code, including a motor vehicle with a gross vehicle weight rating of less than 10,000 pounds.\n**(10) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(11) Vehicle dynamic system**\nThe term vehicle dynamic system means ADAS and any related or integrated systems affecting the stability, control, or motion of the vehicle.",
      "versionDate": "2025-12-12",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-13T19:07:29Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-04-13T19:01:46Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-13T19:02:30Z"
          },
          {
            "name": "Hybrid, electric, and advanced technology vehicles",
            "updateDate": "2026-04-13T19:01:29Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-04-13T19:01:34Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-04-13T19:02:10Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-04-13T19:01:40Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2026-04-13T19:07:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-08T19:45:11Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6688ih.xml"
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
      "title": "ADAS Functionality and Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ADAS Functionality and Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the National Highway Traffic Safety Administration to establish guidelines for advanced driver assistance systems calibration, modifications, and tolerances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:23Z"
    }
  ]
}
```
