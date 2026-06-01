# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4904?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4904
- Title: PHASE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4904
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-04-29T08:07:28Z
- Update date including text: 2026-04-29T08:07:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-06 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-05 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-06 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4904",
    "number": "4904",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "PHASE Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-29T08:07:28Z",
    "updateDateIncludingText": "2026-04-29T08:07:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-06",
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
      "actionDate": "2025-08-05",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-06T21:33:54Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-05T14:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "OR"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4904ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4904\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mrs. Torres of California (for herself and Ms. Bonamici ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Director of the National Institute of Standards and Technology and the Secretary of Transportation to take certain actions to develop physical alternatives to better protect pedestrians and vulnerable road users against traffic incidents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pedestrian Hazard, Awareness, and Safety Expansion Act of 2025 or the PHASE Act of 2025 .\n#### 2. NIST innovative technologies to improve and enhance traffic control devices\nThe Director of the National Institute of Standards and Technology shall transmit to the Secretary of Transportation potential solutions using innovative technologies to improve and enhance traffic control devices to better equip vehicle operators, including bicycles and protect pedestrians and vulnerable road users. The Director shall provide supporting evidence to ensure such potential solutions do not overwhelm, overstimulate, or otherwise distract vehicle operators, including bicyclists or pedestrians. Such potential solutions shall comply with all applicable Federal regulations.\n#### 3. Physical alternatives to protect pedestrians and vulnerable road users\n##### (a) Study\nThe Secretary of Transportation shall carry out a study on developing physical alternatives to better protect pedestrians and vulnerable road users from traffic incidents that\u2014\n**(1)**\nanalyzes urban areas, as determined by the Bureau of the Census, in which pedestrian fatalities have increased in the data available as of the date of enactment of this Act to study where crashes involving pedestrians occur most frequently;\n**(2)**\nexamine physical alternatives to reduce vehicle crashes with vulnerable road users and fatalities, including pedestrians; and\n**(3)**\nstudies intelligent speed assistance and blind spot detection safety systems\u2019 impact on the safety of vulnerable road users including the ability of blind spot detection to detect all road users in a timely manner.\n##### (b) Briefing to Congress\nNot later than 2 years after the date of enactment of this Act, the Secretary shall brief the Committee on Transportation and Infrastructure and the Committee on Appropriations of the House of Representative on the results of the study.\n##### (c) Grant program\nThe Secretary shall establish a grant program to provide grants to cities, Indian Tribes, and municipalities to implement infrastructure that complies with all applicable Federal regulations and the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12131 et seq. ) and improves pedestrian safety, including\u2014\n**(1)**\ninnovative technology for crosswalks;\n**(2)**\nadditional pedestrian facilities both on and off the road;\n**(3)**\nexpanded buffer zones;\n**(4)**\npedestrian crossings;\n**(5)**\nincreased pedestrian accommodation on bridges;\n**(6)**\nupgraded highway traffic signals;\n**(7)**\naccessible pedestrian signals;\n**(8)**\naccessible sidewalks;\n**(9)**\nincreased signage;\n**(10)**\nincreased lighting at crossings;\n**(11)**\nadaptive or intelligent roadway and pedestrian lighting;\n**(12)**\naccessible curb ramps; and\n**(13)**\nmarked crosswalks and grade-separated crossings.\n##### (d) Application\nTo be eligible to receive a grant under subsection (c), an applicant shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated $5,000,000 for each fiscal year to carry out the grant program described under subsection (c).",
      "versionDate": "2025-08-05",
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
        "updateDate": "2025-09-18T18:10:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-05",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr4904",
          "measure-number": "4904",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-05",
          "originChamber": "HOUSE",
          "update-date": "2025-09-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4904v00",
            "update-date": "2025-09-22"
          },
          "action-date": "2025-08-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pedestrian Hazard, Awareness, and Safety Expansion Act of 2025 or the PHASE Act of 2025</strong></p><p>This bill directs the National Institute of Standards and Technology (NIST) and the Department of Transportation (DOT) to\u00a0conduct studies and award grants\u00a0to improve road safety for pedestrians and vulnerable road users.</p><p>Specifically, the bill directs NIST to transmit to DOT potential solutions to improve and enhance traffic control devices using innovative technologies in order to better equip vehicle operators (including bicycles) and protect pedestrians and vulnerable road users.\u00a0</p><p>In addition, DOT must establish a program to provide grants to cities, Indian tribes, and municipalities to implement infrastructure that improves pedestrian safety (e.g., innovative technology for crosswalks, expanded buffer zones, and upgraded highway traffic signals).</p><p>DOT must also carry out a study on developing physical alternatives to better protect pedestrians and vulnerable road users from traffic incidents.</p>"
        },
        "title": "PHASE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4904.xml",
    "summary": {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pedestrian Hazard, Awareness, and Safety Expansion Act of 2025 or the PHASE Act of 2025</strong></p><p>This bill directs the National Institute of Standards and Technology (NIST) and the Department of Transportation (DOT) to\u00a0conduct studies and award grants\u00a0to improve road safety for pedestrians and vulnerable road users.</p><p>Specifically, the bill directs NIST to transmit to DOT potential solutions to improve and enhance traffic control devices using innovative technologies in order to better equip vehicle operators (including bicycles) and protect pedestrians and vulnerable road users.\u00a0</p><p>In addition, DOT must establish a program to provide grants to cities, Indian tribes, and municipalities to implement infrastructure that improves pedestrian safety (e.g., innovative technology for crosswalks, expanded buffer zones, and upgraded highway traffic signals).</p><p>DOT must also carry out a study on developing physical alternatives to better protect pedestrians and vulnerable road users from traffic incidents.</p>",
      "updateDate": "2025-09-22",
      "versionCode": "id119hr4904"
    },
    "title": "PHASE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pedestrian Hazard, Awareness, and Safety Expansion Act of 2025 or the PHASE Act of 2025</strong></p><p>This bill directs the National Institute of Standards and Technology (NIST) and the Department of Transportation (DOT) to\u00a0conduct studies and award grants\u00a0to improve road safety for pedestrians and vulnerable road users.</p><p>Specifically, the bill directs NIST to transmit to DOT potential solutions to improve and enhance traffic control devices using innovative technologies in order to better equip vehicle operators (including bicycles) and protect pedestrians and vulnerable road users.\u00a0</p><p>In addition, DOT must establish a program to provide grants to cities, Indian tribes, and municipalities to implement infrastructure that improves pedestrian safety (e.g., innovative technology for crosswalks, expanded buffer zones, and upgraded highway traffic signals).</p><p>DOT must also carry out a study on developing physical alternatives to better protect pedestrians and vulnerable road users from traffic incidents.</p>",
      "updateDate": "2025-09-22",
      "versionCode": "id119hr4904"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4904ih.xml"
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
      "title": "PHASE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PHASE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pedestrian Hazard, Awareness, and Safety Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Director of the National Institute of Standards and Technology and the Secretary of Transportation to take certain actions to develop physical alternatives to better protect pedestrians and vulnerable road users against traffic incidents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:46Z"
    }
  ]
}
```
