# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4705?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4705
- Title: ACHE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4705
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-03-23T15:38:39Z
- Update date including text: 2026-03-23T15:38:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committees on Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committees on Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committees on Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-24 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committees on Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committees on Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committees on Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-24 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4705",
    "number": "4705",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001220",
        "district": "3",
        "firstName": "Morgan",
        "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
        "lastName": "McGarvey",
        "party": "D",
        "state": "KY"
      }
    ],
    "title": "ACHE Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-23T15:38:39Z",
    "updateDateIncludingText": "2026-03-23T15:38:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committees on Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committees on Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committees on Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-24T21:30:06Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "OR"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4705ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4705\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. McGarvey (for himself, Mr. Huffman , Mr. Tonko , Ms. Salinas , Ms. Tlaib , and Mr. Cohen ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committees on Energy and Commerce , and Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo place a moratorium on the issuance and renewal of certain Federal authorizations for mountaintop removal coal mining until a health study is conducted, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Appalachian Communities Health Equity Act of 2025 or the ACHE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCommunities surrounding mountaintop removal coal mining projects, which involve surface coal mining including blasting with explosives in the steep slope regions of Kentucky, Tennessee, West Virginia, and Virginia, have raised concerns that pollution of the water, air, and soil that results from mountaintop removal coal mining may be causing health crises in their communities.\n**(2)**\nPeer-reviewed scientific research and reports have raised serious concerns about mountaintop removal mining with respect to elevated risks in categories of birth defects studied, including circulatory, respiratory, central nervous system, musculoskeletal, and gastrointestinal.\n**(3)**\nMountaintop removal coal mining has also been associated with elevated levels of adult hospitalizations for chronic pulmonary disorders and hypertension that are elevated as a function of county-level coal production, as are rates of mortality, lung cancer, and chronic heart, lung, and kidney disease. These health problems strike both women and men in mountaintop removal coal mining communities and these elevated levels of disease, defects, and mortality persist even after controlling for other variables.\n**(4)**\nScientific evidence, and the level of public concern, warrant immediate action to stop new mountaintop removal coal mining permits and increase environmental and human health monitoring at existing mountaintop removal coal mining projects while the reported links between health effects and mountaintop removal coal mining are investigated by Federal health agencies.\n**(5)**\nThe National Institute of Environmental Health Sciences is uniquely qualified to manage a working group of Federal health agencies with expertise that is relevant to study of the reported links.\n#### 3. Health study\n##### (a) Study\nThe Director of the National Institute of Environmental Health Sciences, in consultation with the Administrator of the Environmental Protection Agency and the heads of such other Federal agencies as the Director determines appropriate, shall conduct or support a comprehensive study regarding the health impacts, if any, of mountaintop removal coal mining on individuals who reside in communities in close proximity to mountaintop removal coal mining projects.\n##### (b) Report\nThe Director of the National Institute of Environmental Health Sciences shall submit to the Secretary, and make publicly available, a report regarding the results of the study conducted or supported under subsection (a).\n##### (c) Determination\nAfter receipt of the report required under subsection (b), the Secretary shall publish on the website of the Department of Health and Human Services a determination regarding whether mountaintop removal coal mining presents any health risks to individuals who reside in communities in close proximity to mountaintop removal coal mining projects.\n#### 4. Mountaintop removal coal mining Federal authorization moratorium\nNo Federal authorization may be issued or renewed for any mountaintop removal coal mining project, or for any expansion of such a project, by any of the following individuals before the date on which the Secretary publishes a determination under section 3(c) concluding that mountaintop removal coal mining does not present any health risks to individuals who reside in communities in close proximity to mountaintop removal coal mining projects:\n**(1)**\nThe Secretary of the Army, acting through the Chief of Engineers, or a State, under section 404 of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ).\n**(2)**\nThe Administrator of the Environmental Protection Agency, or a State, under section 402 of the Federal Water Pollution Control Act ( 33 U.S.C. 1342 ).\n**(3)**\nThe Secretary of the Interior, acting through the Director of the Office of Surface Mining Reclamation and Enforcement, or a State, under the Surface Mining Control and Reclamation Act of 1977 ( 30 U.S.C. 1201 et seq. ).\n#### 5. Mountaintop removal coal mining monitoring\n##### (a) Monitoring requirement\nAny person that conducts a mountaintop removal coal mining project shall\u2014\n**(1)**\nwith respect to the site of the project, carry out monitoring for pollution that occurs as a result of the project, including\u2014\n**(A)**\ncontinuous monitoring for water, air, and noise pollution; and\n**(B)**\nconsistent monitoring for soil pollution; and\n**(2)**\nbased on the results of the monitoring carried out under paragraph (1)\u2014\n**(A)**\nidentify any pollution that occurs as a result of the project; and\n**(B)**\nidentify ways in which individuals who reside in communities in close proximity to the project might be exposed to such pollution.\n##### (b) Results of monitoring\n**(1) Submission to Secretary**\nEach person that carries out monitoring under subsection (a)(1) for a mountaintop removal coal mining project shall submit to the Secretary, on a monthly basis, the results of such monitoring.\n**(2) Public availability**\nNot later than 7 days after the date on which the Secretary receives results under paragraph (1), the Secretary shall make such results publicly available on the website of the Department of Health and Human Services in a searchable database format.\n##### (c) Enforcement\nIf a person that conducts a mountaintop removal coal mining project fails to comply with either subsection (a) or (b) with respect to the project, no Federal authorization may be issued or renewed for the project, or for any expansion of the project, by any of the following individuals:\n**(1)**\nThe Secretary of the Army, acting through the Chief of Engineers, or a State, under section 404 of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ).\n**(2)**\nThe Administrator of the Environmental Protection Agency, or a State, under section 402 of the Federal Water Pollution Control Act ( 33 U.S.C. 1342 ).\n**(3)**\nThe Secretary of the Interior, acting through the Director of the Office of Surface Mining Reclamation and Enforcement, or a State, under the Surface Mining Control and Reclamation Act of 1977 ( 30 U.S.C. 1201 et seq. ).\n##### (d) Applicability\nThe requirements under subsections (a) and (b) shall terminate on the date on which the Secretary publishes the determination described in section 3(c).\n#### 6. Federal cost fee\n##### (a) Collection and assessment\nThe Secretary of the Interior, acting through the Director of the Office of Surface Mining Reclamation and Enforcement, shall assess and collect a one-time fee from each person that, as of the date of the enactment of this Act, is conducting or has previously completed a mountaintop removal coal mining project in the United States, in an amount sufficient to recover the Federal cost of implementing sections 3 and 5.\n##### (b) Use of fee\nAmounts collected under this section may be used, to the extent and in the amount provided in advance in appropriations Acts, only to pay the Federal cost of carrying out sections 3 and 5.\n#### 7. Definitions\nIn this Act:\n**(1) Federal authorization**\nThe term Federal authorization means a permit, license, or other authorization that is issued by a Federal agency.\n**(2) Mountaintop removal coal mining**\nThe term mountaintop removal coal mining means surface coal mining that\u2014\n**(A)**\nuses blasting with explosives; and\n**(B)**\nis carried out in the steep slope regions of Kentucky, Tennessee, West Virginia, and Virginia.\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(4) Steep slope**\nThe term steep slope has the meaning given the term in section 515(d)(4) of the Surface Mining Control and Reclamation Act of 1977 ( 30 U.S.C. 1265(d)(4) ).",
      "versionDate": "2025-07-23",
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
        "name": "Environmental Protection",
        "updateDate": "2026-03-23T15:38:39Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4705ih.xml"
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
      "title": "ACHE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACHE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Appalachian Communities Health Equity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To place a moratorium on the issuance and renewal of certain Federal authorizations for mountaintop removal coal mining until a health study is conducted, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:21Z"
    }
  ]
}
```
