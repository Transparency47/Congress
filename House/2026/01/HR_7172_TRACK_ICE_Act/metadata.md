# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7172
- Title: TRACK ICE Act
- Congress: 119
- Bill type: HR
- Bill number: 7172
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-04-17T08:07:16Z
- Update date including text: 2026-04-17T08:07:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7172",
    "number": "7172",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001130",
        "district": "30",
        "firstName": "Jasmine",
        "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
        "lastName": "Crockett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "TRACK ICE Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:16Z",
    "updateDateIncludingText": "2026-04-17T08:07:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-21T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
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
      "sponsorshipDate": "2026-01-22",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "MI"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7172ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7172\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Ms. Crockett (for herself and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 49, United States Code, to limit eligibility of certain aviation privacy programs for immigration aircraft operations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency Requirements for Aircraft Carriers to Know Immigration Conduct and Enforcement Act or the TRACK ICE Act .\n#### 2. Limitation on FAA privacy programs for immigration aircraft operators\nSection 44114 of title 49, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Applicability to certain aircraft operations A private aircraft owner or operator shall not be eligible for withholding of information under subsections (a) and (b) for any aircraft operation that is\u2014 (1) operated by, under contract or subcontract with, or on behalf of U.S. Immigration and Customs Enforcement or Customs and Border Protection; (2) used for the purpose of detention, deportation, or the transport of individuals in the custody of the Secretary of Homeland Security in connection with the enforcement of the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )); and (3) receives Federal funding or any other financial assistance for operation described in paragraphs (1) and (2). .\n#### 3. Transparency of flight data\n##### (a) In general\nNot later than 72 hours after each aircraft operation carried out by the Department of Homeland Security, including U.S. Immigration and Customs Enforcement or Customs and Border Protection, or the Coast Guard for the purpose of detention, deportation, or the transport of individuals in the custody of the Secretary of Homeland Security in connection with the enforcement of the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )), the Secretary of Homeland Security shall publish flight data for such aircraft operation in a manner that is accessible to the public.\n##### (b) Flight data defined\nIn this section, the term flight data includes\u2014\n**(1)**\nthe date and time of departure at origin airport;\n**(2)**\nthe date and time of arrival at arrival airport;\n**(3)**\nthe departure airport\u2019s International Civil Aviation Organization (ICAO) code and the ICE Air mission designation;\n**(4)**\nthe arrival airport\u2019s ICAO code and the ICE Air mission designation;\n**(5)**\nthe aircraft registration number;\n**(6)**\nthe ICAO aircraft identification code;\n**(7)**\nthe number of individuals detained by U.S. Immigration and Customs Enforcement or other immigration enforcement agency who boarded and deplaned at each departure and arrival location; and\n**(8)**\ndemographic data for each detainee transported on each individual departure and arrival flight leg (identified by ICAO airport codes), including\u2014\n**(A)**\nnationality;\n**(B)**\nsex;\n**(C)**\nage category (grouped as 0\u201310; 11\u201317; 18\u201350; 51+);\n**(D)**\nfamily composition category (specifying, at a minimum, single adult, unaccompanied child, or family unit); and\n**(E)**\nthe type and quantity of any restraints used for the duration of the flights on each detained individual, such as handcuffs, shackles on arms and legs, or full-body restraint device.",
      "versionDate": "2026-01-21",
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
        "updateDate": "2026-02-13T18:38:06Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7172ih.xml"
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
      "title": "TRACK ICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRACK ICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transparency Requirements for Aircraft Carriers to Know Immigration Conduct and Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to limit eligibility of certain aviation privacy programs for immigration aircraft operations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T04:48:18Z"
    }
  ]
}
```
