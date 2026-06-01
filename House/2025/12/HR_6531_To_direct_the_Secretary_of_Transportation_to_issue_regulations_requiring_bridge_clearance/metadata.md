# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6531?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6531
- Title: Bridges not Bumpers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6531
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-02-03T09:05:40Z
- Update date including text: 2026-02-03T09:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- 2026-02-02 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- 2026-02-02 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6531",
    "number": "6531",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000606",
        "district": "16",
        "firstName": "George",
        "fullName": "Rep. Latimer, George [D-NY-16]",
        "lastName": "Latimer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Bridges not Bumpers Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:40Z",
    "updateDateIncludingText": "2026-02-03T09:05:40Z"
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
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-02-02T19:31:59Z",
                "name": "Referred to"
              }
            },
            "name": "Highways and Transit Subcommittee",
            "systemCode": "hspw12"
          },
          {
            "activities": {
              "item": {
                "date": "2026-02-02T19:31:59Z",
                "name": "Referred to"
              }
            },
            "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
            "systemCode": "hspw14"
          }
        ]
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-09T17:05:40Z",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CT"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NJ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MD"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CT"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6531ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6531\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Latimer (for himself, Mr. Bresnahan , Mr. Larson of Connecticut , Mr. Mackenzie , and Mr. Kennedy of New York ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Transportation to issue regulations requiring bridge clearance information in certain GPS navigation devices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bridges not Bumpers Act of 2025 .\n#### 2. DOT bridge clearance strike working group\n##### (a) Establishment\nThe Secretary of Transportation shall establish a bridge clearance strike working group to make recommendations on ways to improve public-private data sharing regarding bridge clearance and commercial motor vehicle route data.\n##### (b) Membership\nThe working group established under subsection (a) shall include representatives from\u2014\n**(1)**\nthe Federal Highway Administration;\n**(2)**\nThe Federal Railroad Administration;\n**(3)**\nthe Federal Motor Carrier Safety Administration;\n**(4)**\nState departments of transportation;\n**(5)**\ntrucking organizations;\n**(6)**\nproducers of GPS navigation systems;\n**(7)**\nlaw enforcement agencies;\n**(8)**\ncompanies that rent or lease covered rental vehicles directly to consumers; and\n**(9)**\nClass I, II, and III railroad carriers.\n##### (c) Contents of recommendations\nThe recommendations required under subsection (a) shall\u2014\n**(1)**\ninclude ways to improve the availability of information and route signs specific to commercial motor vehicles on GPS navigation tools;\n**(2)**\naddress potential liability issues if bridge clearance information shared between public and private partners is not accurate;\n**(3)**\naddress ways to improve truck driver knowledge about bridge strikes that may include a section on commercial driver\u2019s license tests about bridge strikes;\n**(4)**\ninclude ways for companies that rent covered rental vehicles to clearly label their vehicles with height and weight information;\n**(5)**\ninclude ways for companies that rent covered rental vehicles to provide notice, whether orally or written, of vehicle height to individuals who rent or lease a vehicle, and warn such individuals to look out for road signs about vehicle height; and\n**(6)**\naddress what public or private funding streams would be necessary to incorporate bridge clearance and truck route data into GPS navigation tools.\n##### (d) Regulations\nNot later than 1 year after the working group issues recommendations under subsection (a), the Secretary shall issue such regulations as are necessary to implement such recommendations.\n##### (e) Immunity from certain liability\nA GPS administrator shall be immune from liability in a civil action in any court for any injury resulting from the inclusion of information on clearance heights of bridges, tunnels, or underpasses provided by a State or the Federal Government.\n#### 3. Sense of Congress on national education campaign\n##### (a) In general\nIt is the sense of Congress that\u2014\n**(1)**\nthe Secretary, in coordination with the working group established under section 3, should conduct a national education campaign to prevent and raise awareness on bridge strikes by commercial motor vehicles; and\n**(2)**\nthe national education campaign should be targeted towards\u2014\n**(A)**\neducational programs for commercial drivers;\n**(B)**\nindependent operator businesses; and\n**(C)**\nmotor carrier associations.\n#### 4. National clearinghouse for bridge and tunnel clearance strikes\n##### (a) Establishment\nThe Secretary of Transportation shall establish a national clearinghouse for bridge and tunnel clearance strikes that\u2014\n**(1)**\nserves as a centralized repository for data collection, management, and dissemination of best practices for prevention of bridge strikes by commercial motor vehicles; and\n**(2)**\nis modeled after the prototype developed by the National Cooperative Highway Research Program of the National Academies in the publication titled Guide for Preventing and Mitigating the Risk of Bridge and Tunnel Strikes by Motor Vehicles (NCHRP 08\u2013139).\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary $5,000,000 to carry out this section.\n#### 5. Grants for research on potential improvements to roadway, bridge, and tunnel locations\n##### (a) Establishment\nThe Secretary shall establish a grant program to provide grants to eligible entities to conduct research using the clearinghouse established under section 4 to\u2014\n**(1)**\nidentify roadway, bridge, and tunnel locations for potential infrastructure improvement projects to mitigate bridge and tunnel clearance strikes;\n**(2)**\nconduct basic, preliminary engineering tasks to analyze alternative bridge strike mitigation options and identify preferred mitigation alternative recommendations; and\n**(3)**\nassess the effectiveness of currently implemented and future countermeasures against bridge and tunnel clearance strikes and strategies and programs to reduce such strikes.\n##### (b) Eligible entities\nAn entity eligible to receive a grant under this section is\u2014\n**(1)**\na State department of transportation;\n**(2)**\na unit of local government;\n**(3)**\na metropolitan planning organization;\n**(4)**\nClass II and Class III railroads; and\n**(5)**\na transportation safety organization.\n##### (c) Prioritization\nIn providing grants under this section, the Secretary shall prioritize eligible entities located in States with a high incidence of bridge strikes, as determined by the Secretary.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated $5,000,000 for each of fiscal years 2026 through 2030 to carry out this section.\n#### 6. Definitions of commercial motor vehicle\nIn this Act:\n**(1) Commercial motor vehicle**\nThe term commercial motor vehicle has the meaning given the term in section 31132 of title 49, United States Code.\n**(2) Covered rental vehicle**\nThe term covered rental vehicle means a motor vehicle that\u2014\n**(A)**\nis self-propelled or towed and used on public streets, roads, and highways except a truck tractor;\n**(B)**\nhas a gross vehicle weight rating of at least 5,700 pounds;\n**(C)**\nis rented without a driver for an initial term of less than 4 months; and\n**(D)**\nis part of a motor vehicle fleet of 5 or more motor vehicles that are used for rental purposes by a rental company.",
      "versionDate": "2025-12-09",
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
        "updateDate": "2026-01-09T16:32:23Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6531ih.xml"
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
      "title": "Bridges not Bumpers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T09:38:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bridges not Bumpers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T09:38:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to issue regulations requiring bridge clearance information in certain GPS navigation devices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T09:33:27Z"
    }
  ]
}
```
