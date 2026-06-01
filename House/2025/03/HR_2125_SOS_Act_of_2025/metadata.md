# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2125?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2125
- Title: SOS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2125
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-06-06T14:17:56Z
- Update date including text: 2025-06-06T14:17:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-14 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-14 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-14 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-14 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2125",
    "number": "2125",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000590",
        "district": "7",
        "firstName": "Mark",
        "fullName": "Rep. Green, Mark E. [R-TN-7]",
        "lastName": "Green",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "SOS Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-06T14:17:56Z",
    "updateDateIncludingText": "2025-06-06T14:17:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T22:08:34Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-14T13:08:05Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "VA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NC"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "TN"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "SC"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "GA"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "FL"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "MN"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2125ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2125\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Green of Tennessee (for himself, Mrs. Kiggans of Virginia , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a National Commission on the Maritime Industrial Base, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Save Our Shipyards Act of 2025 or the SOS Act of 2025 .\n#### 2. Establishment\nThere is established a commission to be known as the National Commission on the Maritime Industrial Base or the SOS Commission (in this Act referred to as the Commission ).\n#### 3. Functions\n##### (a) Investigation and Study\nThe Commission shall complete an investigation and study the condition of the United States maritime industry and any impediments to a strong and competitive United States maritime industry, with a particular focus on the needs of the United States military, including shipyards, shipbuilding and repairs, harbors, and skilled workforce.\n##### (b) Policy recommendations\nBased on the results of the investigation and study under subsection (a), the Commission shall recommend to the President and Congress policies which should be adopted to\u2014\n**(1)**\nachieve the national goal of a strong United States maritime industry which will help to provide for the national defense;\n**(2)**\nrevitalize the United States naval fleet and maintain that fleet at a level sufficient to contribute to the national defense;\n**(3)**\nfoster a viable United States shipbuilding industry to provide an industrial base for meeting present and future military and civilian shipbuilding needs; and\n**(4)**\nreduce the loss of seafaring and shipbuilding jobs for United States citizens so as to ensure the existence of a reliable maritime labor force.\n#### 4. Specific matters to be addressed\nIn investigating and studying under section 3, the Commission shall investigate and study the following:\n**(1) Current condition of united states maritime industry**\nThe current condition of the United States maritime industry, including how the condition of the industry is likely to change over the next 10 years following the date of enactment of this Act.\n**(2) National defense**\nThe adequacy of the United States maritime industry to ensure the national defense.\n**(3) Maritime labor**\nThe adequacy of skilled mariners and shipyard workers, and the level of training of United States mariners at training facilities in the United States.\n**(4) Impediments to strong and competitive maritime industry**\nWhether the Federal Government should take any legislative or administrative actions related to the United States maritime industry to strengthen our national security, including\u2014\n**(A)**\nthe tax and regulatory burden on the US maritime industry;\n**(B)**\nincentives to encourage investment in United States shipyards and shipbuilding;\n**(C)**\nincentives for personnel to enter the skilled labor workforce for shipbuilding;\n**(D)**\nthe effect of subsidies and other financial assistance by foreign governments to their vessel operators and shipbuilders;\n**(E)**\nthe effects of great power competition and a potential war on United States naval and maritime forces; and\n**(F)**\nthe prioritization of national security related matters in regulatory review and approval processes.\n#### 5. Membership; Administrative matters\n##### (a) Appointment\nThe Commission shall be composed of 15 voting commissioners and 7 non-voting members appointed in the following manner:\n**(1)**\n5 voting commissioners appointed by the President.\n**(2)**\n7 non-voting members appointed by the President who shall be chosen from the list described in subsection (c).\n**(3)**\n3 voting commissioners appointed by the majority leader of the Senate.\n**(4)**\n3 voting commissioners appointed by the Speaker of the House of Representatives.\n**(5)**\n2 voting commissioners appointed by the minority leader of the Senate.\n**(6)**\n2 voting commissioners appointed by the minority leader of the House of Representatives.\n##### (b) Qualifications for voting commissioners\nVoting commissioners appointed under subsection (a) shall be appointed from among United States citizens who are experts in commercial shipping, international trade, maritime industry policy and regulations, and related disciplines and who can represent United States-flagged vessel operators (including domestic passenger vessel operators), seafaring and shipbuilding labor, shipbuilders, shippers, and the financial community with expertise in maritime matters.\n##### (c) Qualifications of non-Voting members\nOne non-voting member appointed under subsection (a) shall be appointed from each of the following:\n**(1)**\nThe Navy.\n**(2)**\nThe Coast Guard.\n**(3)**\nThe United States Maritime Service.\n**(4)**\nThe Marine Corps.\n**(5)**\nThe United States Naval War College.\n**(6)**\nThe Maritime Administration.\n**(7)**\nThe United States Merchant Maritime Academy.\n##### (d) Terms of office\nMembers and commissioners shall be appointed for the duration of the Commission.\n##### (e) Initial meeting\nNot later than 90 days after two-thirds of the voting commissioners have been appointed under this section, the Commission shall be considered active and the Commission shall hold a first meeting.\n##### (f) Vacancies\nA vacancy in the Commission shall be filled in the manner in which the original appointment was made.\n##### (g) Travel expenses\nMembers and commissioners shall serve without pay but shall receive travel expenses, including per diem in lieu of subsistence, in accordance with subchapter I of chapter 57 of title 5, United States Code.\n##### (h) Chair\nThe President, in consultation with the majority leader of the Senate and the Speaker of the House of Representatives, shall designate the Chair of the Commission from among its voting members.\n##### (i) Quorum\nFor the purposes of conducting meetings of the Commission, a quorum of the Commission shall be considered the presence of 10 voting commissioners.\n##### (j) Commission panels\nThe Chair shall establish such panels consisting of voting commissioners as the Chair determines appropriate to carry out the functions of the Commission.\n##### (k) Staff\nThe Commission may appoint and fix the pay of such personnel as the Commission determines appropriate.\n##### (l) Staff of Federal agencies\nUpon request of the Commission, the head of any department or agency of the United States may detail, on a reimbursable basis, any of the personnel of that department or agency to the Commission to assist it in carrying out its duties under this title.\n##### (m) Administrative support services\nUpon request of the Commission, the Administrator of General Services shall provide to the Commission, on a reimbursable basis, the administrative support services necessary for the Commission to carry out its duties under this title.\n##### (n) Obtaining official data\nThe Commission may secure directly from any department or agency of the United States information (other than information required by any statute of the United States to be kept confidential by such department or agency) necessary for the Commission to carry out its duties under this title. Upon request of the Commission, the head of that department or agency shall furnish such nonconfidential information to the Commission.\n##### (o) Security clearances for commissioners, members, and staff\nThe appropriate Federal departments or agencies shall cooperate with the Commission in expeditiously providing to commissioners, members, and staff appropriate security clearances to the extent possible pursuant to existing procedures and requirements, except that no person may be provided with access to classified information under this Act without the appropriate security clearances.\n#### 6. Report\n##### (a) In general\nNot later than 1 year after the date on which the Commission holds the first meeting under section 5, the Commission shall transmit to the President and Congress a report on the activities of the Commission, including recommendations made by the Commission under section 3(b) which shall be considered by the relevant congressional committees for possible legislative action.\n##### (b) Classification\nThe report under subsection (a) shall be transmitted in an unclassified form but may include a classified annex.\n#### 7. Termination\nThe Commission shall terminate on the date that is 30 days after the transmittal of the report under section 6.",
      "versionDate": "2025-03-14",
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
        "updateDate": "2025-05-21T00:58:40Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2125ih.xml"
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
      "title": "SOS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SOS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save Our Shipyards Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a National Commission on the Maritime Industrial Base, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:01Z"
    }
  ]
}
```
