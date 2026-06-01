# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4843?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4843
- Title: CLEAR ID Act
- Congress: 119
- Bill type: HR
- Bill number: 4843
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2026-05-22T08:08:33Z
- Update date including text: 2026-05-22T08:08:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-01 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-04 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-01 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-04 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4843",
    "number": "4843",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
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
    "title": "CLEAR ID Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:33Z",
    "updateDateIncludingText": "2026-05-22T08:08:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-04",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-04T20:20:35Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-01T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "OR"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "TX"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
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
      "sponsorshipDate": "2025-10-03",
      "state": "DC"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MD"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CO"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4843ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4843\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Ms. Crockett (for herself, Ms. Dexter , and Ms. Johnson of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide that no Federal funds made available to the Department of Homeland Security may be used to carry out any civil immigration enforcement activity under the immigration laws unless each officer conducting such an action is not wearing a mask or facial covering that hides the identity of the officer, and clearly identifies themselves verbally and visibly, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Combating Law Enforcement Anonymity by Requiring Identification Disclosure Act or the CLEAR ID Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThere has been an increase in reported incidents where individuals are illegally impersonating immigration enforcement officers, including but not limited to U.S. Immigration and Customs Enforcement officers across the country.\n**(2)**\nOn June 14, 2025, a man in Chicago, Illinois, was arrested after impersonating a U.S. Immigration and Customs Enforcement officer while possessing a loaded semi-automatic weapon without a concealed carry license.\n**(3)**\nOn June 8, 2025, in Philadelphia, Pennsylvania, a man was arrested after zip-tying a woman and stealing money from a business while impersonating a U.S. Immigration and Customs Enforcement officer.\n**(4)**\nOn April 10, 2025, a woman in Bay County, Florida, was arrested for abducting another woman while impersonating a U.S. Immigration and Customs Enforcement officer while concealing her identity with a face mask.\n**(5)**\nOn January 29, 2025, a man in Sullivan\u2019s Island, South Carolina, was arrested for detaining a group of men while impersonating a U.S. Immigration and Customs Enforcement officer.\n**(6)**\nOn January 26, 2025, a man in Raleigh, North Carolina, was arrested after sexually assaulting a woman while impersonating a U.S. Immigration and Customs Enforcement officer.\n**(7)**\nThe impersonation of a law enforcement officer is a violation of Federal, State, and local laws. It erodes public trust in law enforcement and deters actually law enforcement officers from doing their jobs.\n#### 3. Limitation on use of funds by the Department of Homeland Security\n##### (a) Limitation\nNotwithstanding any other provision of law, and except as provided in subsection (b), no Federal funds made available to the Department of Homleand Security may be used to conduct a civil immigration enforcement action under the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )) unless each covered immigration officer conducting such an action\u2014\n**(1)**\nis not wearing a mask or facial covering that hides the identity of the officer;\n**(2)**\nif the officer uses a vehicle to conduct an official operation in connection with such action, uses only a vehicle that clearly identifies the name of the agency involved in the action; and\n**(3)**\nclearly identifies themselves verbally and visibly by showing identification of the agency that the covered immigration officer represents or is conducting official business on behalf of, including visibly presenting a badge and wearing a uniform that represents the agency involved in the enforcement action.\n##### (b) Exceptions\nSubsection (a) shall not apply if a mask or facial covering is medically necessary or is required to preserve the integrity of an ongoing undercover operation that has been approved in accordance with the criteria described in subsection (c).\n##### (c) Criteria described\nThe criteria described in this subsection for the approval of an undercover operation are the following:\n**(1)**\nThe risk of personal injury to individuals, property damage, financial loss to persons or businesses, damage to reputation, and other harm.\n**(2)**\nThe risk of civil liability or other loss to the Government.\n**(3)**\nThe risk of invasion of privacy or interference with privileged or confidential relationships.\n**(4)**\nThe risk that individuals engaged in the undercover operation may become involved conduct that is unlawful under Federal law.\n**(5)**\nThe suitability of Government participation in the type of activity that is expected to occur during the operation.\n##### (d) Definition\nThe term covered immigration officer means\u2014\n**(1)**\npersonnel of U.S. Customs and Border Protection;\n**(2)**\npersonnel of U.S. Immigration and Customs Enforcement; and\n**(3)**\npersonnel of any other Federal, State, or local agency authorized by the Secretary of Homeland Security to conduct civil immigration enforcement actions under the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )).",
      "versionDate": "2025-08-01",
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
        "name": "Immigration",
        "updateDate": "2025-09-17T17:08:20Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4843ih.xml"
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
      "title": "CLEAR ID Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAR ID Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combating Law Enforcement Anonymity by Requiring Identification Disclosure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that no Federal funds made available to the Department of Homeland Security may be used to carry out any civil immigration enforcement activity under the immigration laws unless each officer conducting such an action is not wearing a mask or facial covering that hides the identity of the officer, and clearly identifies themselves verbally and visibly, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:29Z"
    }
  ]
}
```
