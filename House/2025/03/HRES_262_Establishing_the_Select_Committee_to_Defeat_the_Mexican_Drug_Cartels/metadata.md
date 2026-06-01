# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/262?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/262
- Title: Establishing the Select Committee to Defeat the Mexican Drug Cartels.
- Congress: 119
- Bill type: HRES
- Bill number: 262
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-05-01T08:05:57Z
- Update date including text: 2025-05-01T08:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-27 - IntroReferral: Submitted in House
- 2025-03-27 - IntroReferral: Submitted in House
- Latest action: 2025-03-27: Submitted in House

## Actions

- 2025-03-27 - IntroReferral: Referred to the House Committee on Rules.
- 2025-03-27 - IntroReferral: Submitted in House
- 2025-03-27 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/262",
    "number": "262",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001120",
        "district": "2",
        "firstName": "Dan",
        "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
        "lastName": "Crenshaw",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Establishing the Select Committee to Defeat the Mexican Drug Cartels.",
    "type": "HRES",
    "updateDate": "2025-05-01T08:05:57Z",
    "updateDateIncludingText": "2025-05-01T08:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "FL"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TN"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AR"
    },
    {
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "KY"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "OK"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "J000289",
      "district": "4",
      "firstName": "Jim",
      "fullName": "Rep. Jordan, Jim [R-OH-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Jordan",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "WI"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MS"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "PA"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AR"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AL"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "MO"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "KY"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AZ"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AZ"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "MI"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres262ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 262\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Crenshaw (for himself, Mr. Mast , Mr. Green of Tennessee , Mr. Arrington , Mr. Hill of Arkansas , Mr. Comer , Mr. Cole , Mr. McCaul , Mr. Jordan , Mr. Babin , Mr. Steil , Mr. Guest , Mr. Thompson of Pennsylvania , Mr. Westerman , Mr. Rogers of Alabama , Mr. Williams of Texas , Mr. Bost , Mr. Graves , Mr. Guthrie , Mr. Biggs of Arizona , Mr. Ciscomani , and Mr. Vicente Gonzalez of Texas ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nEstablishing the Select Committee to Defeat the Mexican Drug Cartels.\n#### 1. Select Committee to Defeat the Mexican Drug Cartels\n##### (a) Establishment; composition\n**(1) Establishment**\nThere is hereby established in the House of Representatives a Select Committee to Defeat the Mexican Drug Cartels (hereinafter in this section referred to as the Select Committee ).\n**(2) Composition**\n**(A) In general**\nThe Select Committee shall be composed of not more than 21 Members, Delegates, or the Resident Commissioner appointed by the Speaker, not more than 10 of whom shall be appointed after consultation with the minority leader. The Speaker shall designate one member of the Select Committee as its chair. A vacancy in the membership of the Select Committee shall be filled in the same manner as the original appointment.\n**(B) Other committee assignments**\nThe Select Committee shall include at least one majority Member, delegate, or the resident commissioner from each of the following committees:\n**(i)**\nThe Committee on Appropriations.\n**(ii)**\nThe Committee on the Judiciary.\n**(iii)**\nThe Committee on Homeland Security.\n**(iv)**\nThe Committee on Armed Services.\n**(v)**\nThe Committee on Financial Services.\n**(C) Designation of leadership staff member**\nThe Speaker and the minority leader each may designate a leadership staff member to assist in their capacity as ex officio members, with the same access to Select Committee meetings, hearings, briefings, and materials as employees of the Select Committee and subject to the same security clearance and confidentiality requirements as staff of the Select Committee.\n##### (b) Jurisdiction; functions\n**(1) Legislative jurisdiction**\nThe Select Committee shall not have legislative jurisdiction and shall have no authority to take legislative action on any bill or resolution.\n**(2) Investigative jurisdiction**\nThe sole authority of the Select Committee shall be to investigate and submit policy recommendations on the operations and capabilities of the Mexican drug cartels, to include the international networks that facilitate and enable the Mexican drug cartels and the United States, Mexican, and other government efforts to target and defeat the cartels. The Select Committee may, at its discretion, hold public hearings in connection with any aspect of its investigative functions.\n##### (c) Procedure\n**(1)**\nClause 11(b)(4), clause 11(e), and the first sentence of clause 11(f) of rule X shall apply to the Select Committee.\n**(2)**\nExcept as specified in paragraph (4), the Select Committee shall have the authorities and responsibilities of, and shall be subject to the same limitations and restrictions as, a standing committee of the House, and shall be deemed a committee of the House for all purposes of law or rule.\n**(3)**\n**(A)**\nRules X and XI shall apply to the Select Committee where not inconsistent with this subsection.\n**(B)**\nService on the Select Committee shall not count against the limitations in clause 5(b)(2) of rule X.\n**(C)**\nClause 2(d) of rule X shall not apply to the Select Committee.\n**(D)**\nClause 2(g)(2)(D) of rule XI shall apply to the Select Committee in the same manner as it applies to the Permanent Select Committee on Intelligence.\n##### (d) Records; staff; travel; funding\n**(1)**\nThe appointment and the compensation of staff for the Select Committee shall be subject to regulations issued by the Committee on House Administration.\n**(2)**\n**(A)**\nStaff of employing entities of the House or a joint committee may be detailed to the Select Committee to carry out this resolution and shall be deemed to be staff of the Select Committee.\n**(B)**\nThe Select Committee may request the head of any Federal agency to detail, on a nonreimbursable basis, any of the personnel of the agency to the Select Committee.\n**(3)**\nSection 202(i) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4301(i) ) shall apply with respect to the Select Committee in the same manner as such section applies with respect to a standing committee, except that the selection of any consultant or organization under such section shall be subject to approval by the Speaker.\n##### (e) Reporting\nThe Select Committee may report to the House or any committee from time to time the results of its investigations and studies, together with such detailed findings, policy recommendations, and legislative proposals as it may deem advisable. All such reports shall be submitted to the House by December 31, 2026. All policy recommendations shall be submitted to the relevant standing committees not later than December 31, 2025. The Select Committee shall submit all legislative proposals to the relevant standing committees not later than 60 days after their adoption by the Select Committee.\n##### (f) Publication\n**(1)**\nThe Select Committee shall ensure that reports and proposals prepared in accordance with this subsection shall, upon completion, be made available to the general public in widely accessible formats not later than 30 calendar days following the respective dates for completion set forth in subsection (e).\n**(2)**\nAny report issued by the Select Committee shall be issued in unclassified form but may include a classified annex, a law enforcement-sensitive annex, or both.",
      "versionDate": "2025-03-27",
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
        "name": "Congress",
        "updateDate": "2025-03-28T13:32:08Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres262ih.xml"
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
      "title": "Establishing the Select Committee to Defeat the Mexican Drug Cartels.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T08:48:20Z"
    },
    {
      "title": "Establishing the Select Committee to Defeat the Mexican Drug Cartels.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T08:06:58Z"
    }
  ]
}
```
