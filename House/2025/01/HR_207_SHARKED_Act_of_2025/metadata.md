# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/207?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/207
- Title: SHARKED Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 207
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-03-10T20:36:42Z
- Update date including text: 2026-04-30T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-01-21 14:28:30 - Floor: Mr. Westerman moved to suspend the rules and pass the bill.
- 2025-01-21 14:28:39 - Floor: Considered under suspension of the rules. (consideration: CR H240-242)
- 2025-01-21 14:28:41 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 207.
- 2025-01-21 14:40:52 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H240-241)
- 2025-01-21 14:40:52 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H240-241)
- 2025-01-21 14:40:56 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-01-22 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-01-21 14:28:30 - Floor: Mr. Westerman moved to suspend the rules and pass the bill.
- 2025-01-21 14:28:39 - Floor: Considered under suspension of the rules. (consideration: CR H240-242)
- 2025-01-21 14:28:41 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 207.
- 2025-01-21 14:40:52 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H240-241)
- 2025-01-21 14:40:52 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H240-241)
- 2025-01-21 14:40:56 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-01-22 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/207",
    "number": "207",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "SHARKED Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-10T20:36:42Z",
    "updateDateIncludingText": "2026-04-30T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-01-21",
      "actionTime": "14:40:56",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-01-21",
      "actionTime": "14:40:52",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H240-241)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-01-21",
      "actionTime": "14:40:52",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H240-241)",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-01-21",
      "actionTime": "14:28:41",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 207.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-01-21",
      "actionTime": "14:28:39",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H240-242)",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-01-21",
      "actionTime": "14:28:30",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mr. Westerman moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": [
          {
            "name": "Judiciary Committee",
            "systemCode": "hsju00"
          },
          {
            "name": "Natural Resources Committee",
            "systemCode": "hsii00"
          }
        ]
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-22T17:56:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:27:40Z",
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr207ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 207\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Wittman (for himself, Mr. Webster of Florida , Mr. Soto , and Mr. Veasey ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of Commerce to establish a task force regarding shark depredation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025 .\n#### 2. Shark depredation task force and research projects\n##### (a) Shark depredation task force\n**(1) In general**\nThe Secretary of Commerce shall establish a task force (referred to in this subsection as the task force ) to identify and address critical needs with respect to shark depredation.\n**(2) Membership**\nThe Secretary of Commerce shall appoint individuals to the task force, including\u2014\n**(A)**\n1 representative from\u2014\n**(i)**\neach Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) );\n**(ii)**\neach Marine Fisheries Commission, as such term is defined in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 );\n**(iii)**\nthe fish and wildlife agency of a coastal State from each Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) ); and\n**(iv)**\nthe National Marine Fisheries Service;\n**(B)**\nan individual with expertise in the management of highly migratory species;\n**(C)**\na researcher with expertise in shark management and behavior; and\n**(D)**\na researcher with expertise in shark ecology.\n**(3) Responsibilities**\nThe task force shall\u2014\n**(A)**\ndevelop ways to improve coordination and communication across the fisheries management community and shark research community to address shark depredation;\n**(B)**\nidentify research priorities and funding opportunities for such priorities, including\u2014\n**(i)**\nidentifying shark species involved in interactions;\n**(ii)**\nshark stock assessments;\n**(iii)**\nhow sharks become habituated to humans and thus lead to more interactions between sharks and humans;\n**(iv)**\nhow angler behavior and fishery regulatory frameworks may influence shark interactions;\n**(v)**\ntechniques and strategies to reduce harmful interactions between sharks and humans, including the development and use of non-lethal deterrents;\n**(vi)**\nthe role of healthy shark populations in the ocean food web; and\n**(vii)**\nclimate change impacts on shifting shark populations, prey, and shark behavior;\n**(C)**\ndevelop recommended management strategies to address shark depredation; and\n**(D)**\ncoordinate the development and distribution of educational materials to help the fishing community minimize shark interactions including through changed angler behavior and expectations.\n**(4) Report**\nNot later than 2 years after the date of the enactment of this section, and every 2 years thereafter until the termination of the task force in accordance with paragraph (5), the task force shall submit to Congress a report regarding the findings of the task force.\n**(5) Sunset**\nThe task force shall terminate not later than 7 years after the date on which the Secretary of Commerce establishes the task force.\n**(6) Coastal state defined**\nIn this subsection, the term coastal State \u2014\n**(A)**\nmeans a State of the United States in, or bordering on, the Atlantic Ocean, Pacific Ocean, Arctic Ocean, Gulf of Mexico, or Long Island Sound; and\n**(B)**\nincludes Puerto Rico, the Virgin Islands of the United States, Guam, the Commonwealth of the Northern Mariana Islands, and American Samoa.\n##### (b) Shark depredation research projects\nSection 318(c) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1867(c) ) is amended by adding at the end the following:\n(6) Projects to better understand shark depredation, including identifying what causes increases in shark depredation and determining how to best address shark depredation. .\n##### (c) Effect\nNothing in this section shall be construed to affect the authority and responsibility of the Secretary of Commerce in carrying out the Endangered Species Act of 1973 ( 16 U.S.C. 1351 et seq. ) or the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 et seq. ).",
      "versionDate": "2025-01-03",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr207rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 207\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Received; read twice and referred to the Committee on Commerce, Science, and Transportation\nAN ACT\nTo direct the Secretary of Commerce to establish a task force regarding shark depredation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025 .\n#### 2. Shark depredation task force and research projects\n##### (a) Shark depredation task force\n**(1) In general**\nThe Secretary of Commerce shall establish a task force (referred to in this subsection as the task force ) to identify and address critical needs with respect to shark depredation.\n**(2) Membership**\nThe Secretary of Commerce shall appoint individuals to the task force, including\u2014\n**(A)**\n1 representative from\u2014\n**(i)**\neach Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) );\n**(ii)**\neach Marine Fisheries Commission, as such term is defined in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 );\n**(iii)**\nthe fish and wildlife agency of a coastal State from each Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) ); and\n**(iv)**\nthe National Marine Fisheries Service;\n**(B)**\nan individual with expertise in the management of highly migratory species;\n**(C)**\na researcher with expertise in shark management and behavior; and\n**(D)**\na researcher with expertise in shark ecology.\n**(3) Responsibilities**\nThe task force shall\u2014\n**(A)**\ndevelop ways to improve coordination and communication across the fisheries management community and shark research community to address shark depredation;\n**(B)**\nidentify research priorities and funding opportunities for such priorities, including\u2014\n**(i)**\nidentifying shark species involved in interactions;\n**(ii)**\nshark stock assessments;\n**(iii)**\nhow sharks become habituated to humans and thus lead to more interactions between sharks and humans;\n**(iv)**\nhow angler behavior and fishery regulatory frameworks may influence shark interactions;\n**(v)**\ntechniques and strategies to reduce harmful interactions between sharks and humans, including the development and use of non-lethal deterrents;\n**(vi)**\nthe role of healthy shark populations in the ocean food web; and\n**(vii)**\nclimate change impacts on shifting shark populations, prey, and shark behavior;\n**(C)**\ndevelop recommended management strategies to address shark depredation; and\n**(D)**\ncoordinate the development and distribution of educational materials to help the fishing community minimize shark interactions including through changed angler behavior and expectations.\n**(4) Report**\nNot later than 2 years after the date of the enactment of this section, and every 2 years thereafter until the termination of the task force in accordance with paragraph (5), the task force shall submit to Congress a report regarding the findings of the task force.\n**(5) Sunset**\nThe task force shall terminate not later than 7 years after the date on which the Secretary of Commerce establishes the task force.\n**(6) Coastal state defined**\nIn this subsection, the term coastal State \u2014\n**(A)**\nmeans a State of the United States in, or bordering on, the Atlantic Ocean, Pacific Ocean, Arctic Ocean, Gulf of Mexico, or Long Island Sound; and\n**(B)**\nincludes Puerto Rico, the Virgin Islands of the United States, Guam, the Commonwealth of the Northern Mariana Islands, and American Samoa.\n##### (b) Shark depredation research projects\nSection 318(c) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1867(c) ) is amended by adding at the end the following:\n(6) Projects to better understand shark depredation, including identifying what causes increases in shark depredation and determining how to best address shark depredation. .\n##### (c) Effect\nNothing in this section shall be construed to affect the authority and responsibility of the Secretary of Commerce in carrying out the Endangered Species Act of 1973 ( 16 U.S.C. 1351 et seq. ) or the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 et seq. ).",
      "versionDate": "2025-01-22",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr207eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 207\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo direct the Secretary of Commerce to establish a task force regarding shark depredation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025 .\n#### 2. Shark depredation task force and research projects\n##### (a) Shark depredation task force\n**(1) In general**\nThe Secretary of Commerce shall establish a task force (referred to in this subsection as the task force ) to identify and address critical needs with respect to shark depredation.\n**(2) Membership**\nThe Secretary of Commerce shall appoint individuals to the task force, including\u2014\n**(A)**\n1 representative from\u2014\n**(i)**\neach Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) );\n**(ii)**\neach Marine Fisheries Commission, as such term is defined in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 );\n**(iii)**\nthe fish and wildlife agency of a coastal State from each Regional Fishery Management Council established under section 302(a)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(a)(1) ); and\n**(iv)**\nthe National Marine Fisheries Service;\n**(B)**\nan individual with expertise in the management of highly migratory species;\n**(C)**\na researcher with expertise in shark management and behavior; and\n**(D)**\na researcher with expertise in shark ecology.\n**(3) Responsibilities**\nThe task force shall\u2014\n**(A)**\ndevelop ways to improve coordination and communication across the fisheries management community and shark research community to address shark depredation;\n**(B)**\nidentify research priorities and funding opportunities for such priorities, including\u2014\n**(i)**\nidentifying shark species involved in interactions;\n**(ii)**\nshark stock assessments;\n**(iii)**\nhow sharks become habituated to humans and thus lead to more interactions between sharks and humans;\n**(iv)**\nhow angler behavior and fishery regulatory frameworks may influence shark interactions;\n**(v)**\ntechniques and strategies to reduce harmful interactions between sharks and humans, including the development and use of non-lethal deterrents;\n**(vi)**\nthe role of healthy shark populations in the ocean food web; and\n**(vii)**\nclimate change impacts on shifting shark populations, prey, and shark behavior;\n**(C)**\ndevelop recommended management strategies to address shark depredation; and\n**(D)**\ncoordinate the development and distribution of educational materials to help the fishing community minimize shark interactions including through changed angler behavior and expectations.\n**(4) Report**\nNot later than 2 years after the date of the enactment of this section, and every 2 years thereafter until the termination of the task force in accordance with paragraph (5), the task force shall submit to Congress a report regarding the findings of the task force.\n**(5) Sunset**\nThe task force shall terminate not later than 7 years after the date on which the Secretary of Commerce establishes the task force.\n**(6) Coastal state defined**\nIn this subsection, the term coastal State \u2014\n**(A)**\nmeans a State of the United States in, or bordering on, the Atlantic Ocean, Pacific Ocean, Arctic Ocean, Gulf of Mexico, or Long Island Sound; and\n**(B)**\nincludes Puerto Rico, the Virgin Islands of the United States, Guam, the Commonwealth of the Northern Mariana Islands, and American Samoa.\n##### (b) Shark depredation research projects\nSection 318(c) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1867(c) ) is amended by adding at the end the following:\n(6) Projects to better understand shark depredation, including identifying what causes increases in shark depredation and determining how to best address shark depredation. .\n##### (c) Effect\nNothing in this section shall be construed to affect the authority and responsibility of the Secretary of Commerce in carrying out the Endangered Species Act of 1973 ( 16 U.S.C. 1351 et seq. ) or the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1801 et seq. ).",
      "versionDate": "",
      "versionType": "Engrossed in House"
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
        "actionDate": "2026-03-04",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 349."
      },
      "number": "2314",
      "relationshipDetails": {
        "item": [
          {
            "identifiedBy": "CRS",
            "type": "Identical bill"
          },
          {
            "identifiedBy": "House",
            "type": "Related bill"
          }
        ]
      },
      "title": "SHARKED Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-01-27T16:00:27Z"
          },
          {
            "name": "Aquatic ecology",
            "updateDate": "2025-01-27T16:00:33Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-01-27T16:00:41Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-01-27T16:00:47Z"
          },
          {
            "name": "Fishes",
            "updateDate": "2025-01-27T16:00:53Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2025-01-27T16:01:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-01-24T19:12:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr207",
          "measure-number": "207",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr207v00",
            "update-date": "2025-01-28"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025</strong></p><p>This bill requires the Department of Commerce to establish a task force to address and report to Congress about critical needs with respect to shark depredation. (Shark depredation is the partial or complete removal of a hooked fish by a shark directly from a fishing line before the line is retrieved.) </p><p>The duties of the task force are, among other responsibilities, to (1) develop ways to improve coordination and communication across the fisheries management and shark research communities; (2) identify research priorities and funding opportunities; (3) develop recommended management strategies to address shark depredation; and (4) coordinate the development and distribution of educational materials.</p><p>The bill specifies that the task force must include representatives of each Regional Fishery Management Council, each Marine Fisheries Commission, the fish and wildlife agencies of coastal states, and the National Marine Fisheries Service. The task force must also include researchers\u00a0and others with relevant expertise.</p><p>The task force must report its findings to Congress within two years after the bill's enactment and\u00a0every two years thereafter until the task force is terminated. The task force sunsets within seven years after the date of its establishment.\u00a0\u00a0</p>"
        },
        "title": "SHARKED Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr207.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025</strong></p><p>This bill requires the Department of Commerce to establish a task force to address and report to Congress about critical needs with respect to shark depredation. (Shark depredation is the partial or complete removal of a hooked fish by a shark directly from a fishing line before the line is retrieved.) </p><p>The duties of the task force are, among other responsibilities, to (1) develop ways to improve coordination and communication across the fisheries management and shark research communities; (2) identify research priorities and funding opportunities; (3) develop recommended management strategies to address shark depredation; and (4) coordinate the development and distribution of educational materials.</p><p>The bill specifies that the task force must include representatives of each Regional Fishery Management Council, each Marine Fisheries Commission, the fish and wildlife agencies of coastal states, and the National Marine Fisheries Service. The task force must also include researchers\u00a0and others with relevant expertise.</p><p>The task force must report its findings to Congress within two years after the bill's enactment and\u00a0every two years thereafter until the task force is terminated. The task force sunsets within seven years after the date of its establishment.\u00a0\u00a0</p>",
      "updateDate": "2025-01-28",
      "versionCode": "id119hr207"
    },
    "title": "SHARKED Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025 or the SHARKED Act of 2025</strong></p><p>This bill requires the Department of Commerce to establish a task force to address and report to Congress about critical needs with respect to shark depredation. (Shark depredation is the partial or complete removal of a hooked fish by a shark directly from a fishing line before the line is retrieved.) </p><p>The duties of the task force are, among other responsibilities, to (1) develop ways to improve coordination and communication across the fisheries management and shark research communities; (2) identify research priorities and funding opportunities; (3) develop recommended management strategies to address shark depredation; and (4) coordinate the development and distribution of educational materials.</p><p>The bill specifies that the task force must include representatives of each Regional Fishery Management Council, each Marine Fisheries Commission, the fish and wildlife agencies of coastal states, and the National Marine Fisheries Service. The task force must also include researchers\u00a0and others with relevant expertise.</p><p>The task force must report its findings to Congress within two years after the bill's enactment and\u00a0every two years thereafter until the task force is terminated. The task force sunsets within seven years after the date of its establishment.\u00a0\u00a0</p>",
      "updateDate": "2025-01-28",
      "versionCode": "id119hr207"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr207ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr207rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr207eh.xml"
        }
      ],
      "type": "Engrossed in House"
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
      "title": "SHARKED Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Commerce to establish a task force regarding shark depredation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:33:44Z"
    },
    {
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "SHARKED Act of 2025",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-01-24T01:08:24Z"
    },
    {
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-01-24T01:08:24Z"
    },
    {
      "title": "SHARKED Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-23T02:23:19Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Supporting the Health of Aquatic systems through Research Knowledge and Enhanced Dialogue Act of 2025",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-01-23T02:23:17Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "SHARKED Act of 2025",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-01-23T02:23:17Z"
    }
  ]
}
```
