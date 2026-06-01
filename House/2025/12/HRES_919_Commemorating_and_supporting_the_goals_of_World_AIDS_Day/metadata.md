# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/919?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/919
- Title: Commemorating and supporting the goals of World AIDS Day.
- Congress: 119
- Bill type: HRES
- Bill number: 919
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2025-12-05T16:17:51Z
- Update date including text: 2025-12-05T16:17:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-02 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-02 - IntroReferral: Submitted in House
- 2025-12-02 - IntroReferral: Submitted in House
- Latest action: 2025-12-02: Submitted in House

## Actions

- 2025-12-02 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-02 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-02 - IntroReferral: Submitted in House
- 2025-12-02 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/919",
    "number": "919",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000607",
        "district": "2",
        "firstName": "Mark",
        "fullName": "Rep. Pocan, Mark [D-WI-2]",
        "lastName": "Pocan",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Commemorating and supporting the goals of World AIDS Day.",
    "type": "HRES",
    "updateDate": "2025-12-05T16:17:51Z",
    "updateDateIncludingText": "2025-12-05T16:17:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-12-02T15:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-02T15:02:45Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "PA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "TN"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "GA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "WI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "DC"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "AL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "FL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MI"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres919ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 919\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Mr. Pocan (for himself, Mr. Fitzpatrick , Ms. Barrag\u00e1n , Ms. Brownley , Mr. Cohen , Mr. Davis of Illinois , Mr. Johnson of Georgia , Ms. Kelly of Illinois , Ms. Moore of Wisconsin , Ms. Norton , Mr. Quigley , Ms. Sewell , Mr. Soto , Mr. Thanedar , Mr. Torres of New York , Ms. Vel\u00e1zquez , and Mrs. Watson Coleman ) submitted the following resolution; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nCommemorating and supporting the goals of World AIDS Day.\nThat the House of Representatives\u2014\n**(1)**\nencourages people around the world to work to achieve the goal of 0 new human immunodeficiency virus (referred to in this resolution as HIV ) transmissions, 0 discrimination, and 0 deaths related to acquired immunodeficiency syndrome (referred to in this resolution as AIDS ), in order to end the HIV epidemic in the United States and around the world by 2030;\n**(2)**\nencourages Federal, State, and local governments, including their public health agencies, and community-based organizations to share and disseminate U=U (Undetectable=Untransmittable) information;\n**(3)**\ncommends the efforts and achievements in combating HIV and AIDS through the Ryan White HIV/AIDS Treatment Extension Act of 2009 ( Public Law 111\u201387 ; 123 Stat. 2885), the Minority HIV/AIDS Initiative, the Housing Opportunities for Persons With AIDS Program, the Centers for Disease Control and Prevention, the National Institutes of Health, the Substance Abuse and Mental Health Services Administration, the Office of Minority Health, and the Office of the Secretary of Health and Human Services;\n**(4)**\ncommends the efforts and achievements in combating HIV and AIDS made by the President's Emergency Plan for AIDS Relief (referred to in this resolution as PEPFAR ), the Global Fund to Fight AIDS, Tuberculosis and Malaria, and the Joint United Nations Programme on HIV/AIDS;\n**(5)**\nsupports continued funding for prevention, care, and treatment services and research programs for communities impacted by HIV and people living with HIV in the United States and globally;\n**(6)**\nurges, in order to ensure that an AIDS-free generation is achievable, rapid action by all countries toward further expansion and scale-up of antiretroviral treatment and prevention programs, including efforts to reduce disparities and improve access to life-saving medications for children;\n**(7)**\nencourages the scaling up of comprehensive prevention services, including biomedical and structural interventions and new long-acting preexposure prophylaxis options, to ensure inclusive access to programs and appropriate resources for all people at risk of contracting HIV, especially in communities disproportionately impacted by the disease, as these groups make up the majority of new HIV diagnoses in the United States and prevention efforts should specifically reach these groups;\n**(8)**\nsupports the robust funding of all aspects of research and development of the next generation of treatment and prevention options through the National Institutes of Health and partner institutions, including the development of a vaccine and cure for HIV, as well as treatment and prevention options for significant HIV comorbidities, such as sexually transmitted infections and tuberculosis;\n**(9)**\ncalls for renewed focus on HIV-related vulnerabilities of women and girls, including women and girls at risk for, or who have survived, violence or faced discrimination as a result of the disease;\n**(10)**\nsupports continued leadership by the United States in domestic, bilateral, multilateral, and private sector efforts to fight HIV;\n**(11)**\nencourages input from civil society in the development and implementation of domestic and global HIV policies and programs that guide the response to the disease with specific measures for transparency and accountability;\n**(12)**\nencourages and supports greater degrees of ownership and shared responsibility by developing countries in order to ensure the sustainability of the domestic responses to HIV by those countries; and\n**(13)**\nurges other members of the international community to sustain and scale up their support for, and financial contributions to, efforts around the world to combat HIV.",
      "versionDate": "2025-12-02",
      "versionType": "IH"
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
        "updateDate": "2025-12-05T16:17:51Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres919ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commemorating and supporting the goals of World AIDS Day.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T09:18:29Z"
    },
    {
      "title": "Commemorating and supporting the goals of World AIDS Day.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T09:06:20Z"
    }
  ]
}
```
