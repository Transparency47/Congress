# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3566?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3566
- Title: ANCHOR for Military Families Act
- Congress: 119
- Bill type: HR
- Bill number: 3566
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-03-25T08:06:05Z
- Update date including text: 2026-03-25T08:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3566",
    "number": "3566",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000621",
        "district": "6",
        "firstName": "Emily",
        "fullName": "Rep. Randall, Emily [D-WA-6]",
        "lastName": "Randall",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "ANCHOR for Military Families Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:05Z",
    "updateDateIncludingText": "2026-03-25T08:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:04:35Z",
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "VA"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "OH"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "NC"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "VA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-09",
      "state": "FL"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "WA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "LA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "PA"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "TX"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "WA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "WA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "MP"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "MA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3566ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3566\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Ms. Randall (for herself and Mr. Wittman ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to require the Secretary of Defense to provide information on relocation assistance programs when a member of the Armed Forces receives orders for a change of permanent station, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Assuring Navigation of Compact Help for Ongoing Relocation for Military Families Act or the ANCHOR for Military Families Act .\n#### 2. Provision of Information Regarding Relocation Assistance Programs for Members Receiving Orders for a Change of Permanent Station\n##### (a) In General\nSection 1056 of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A), by striking and community orientation and inserting community orientation, education systems, school enrollment procedures, and State-specific provisions under the Interstate Compact on Educational Opportunity for Military Children ;\n**(B)**\nin subparagraph (C), by striking and community orientation and inserting community orientation, and educational resources for dependent children, including school transition assistance, academic continuity, and special education services ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(E) Educational planning and support services for dependent children with disabilities, including procedures for transferring individualized education programs and coordinating with the Exceptional Family Member Program. ;\n**(2)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively; and\n**(3)**\nby inserting after subsection (d) the following new subsection:\n(e) Provision of Information on Program (1) The Secretary of Defense shall ensure that members of the armed forces and the families of those members are provided information regarding available assistance under this section and any other assistance relating to a change of permanent station available under any other provision of law. (2) The Secretary shall ensure that information required to be provided under this subsection is provided to a member of the armed forces and the family of that member not later than 45 days before the date on which a change of permanent station takes effect for that member. (3) The information provided under this subsection shall include\u2014 (A) information on family assistance programs authorized under section 1788 of this title, including financial planning resources, spouse employment support, and community integration services; (B) guidance on available housing assistance, including on-base housing options, rental protections, and resources for off-base relocation; (C) mental health and well-being support services, including those accessible during the period of transition for a change of permanent station; (D) educational resources for dependent children, including school transition assistance and special education services; (E) information on available legal and financial counseling programs; and (F) any other assistance programs that support members of the armed forces and their families during relocation. (4) The Secretary of Defense shall\u2014 (A) incorporate the information required to be provided under this subsection into accessible materials and briefings provided to members of the armed forces relating to a change of permanent station; (B) ensure that the program under this section provides accessible materials and briefings at military installations and through online resources; (C) develop a communication strategy, including digital outreach and printed materials, to increase awareness of the program under this section and assistance available under other provisions of law relating to a change of permanent station; and (D) assess the satisfaction of members of the armed forces and their families with the information provided under this subsection. .\n##### (b) Report\nNot later than one year after the date of enactment of this Act, and annually thereafter for three years, the Secretary of Defense shall provide to the Committees on Armed Services of the Senate and the House of Representatives a briefing on the implementation of the amendments made by this section. Such briefing shall include\u2014\n**(1)**\nthe status of efforts to integrate information required to be provided by subsection (e) of section 1056 of title 10, United States Code, as added by subsection (a) of this section, into accessible materials and briefings provided to members of the Armed Forces and their families relating to a change of permanent station;\n**(2)**\nan assessment of the awareness by members of the Armed Forces and their families of available programs in support of a change of permanent station; and\n**(3)**\nany recommendations of the Secretary for improving the dissemination of information related to relocation and family assistance programs.",
      "versionDate": "2025-05-21",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-11-18",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "3185",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ANCHOR for Military Families Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-20T12:34:13Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3566ih.xml"
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
      "title": "ANCHOR for Military Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ANCHOR for Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Assuring Navigation of Compact Help for Ongoing Relocation for Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to require the Secretary of Defense to provide information on relocation assistance programs when a member of the Armed Forces receives orders for a change of permanent station, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:37Z"
    }
  ]
}
```
