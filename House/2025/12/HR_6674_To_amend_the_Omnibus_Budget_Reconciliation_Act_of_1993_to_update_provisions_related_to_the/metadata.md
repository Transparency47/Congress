# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6674?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6674
- Title: CLAIM Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6674
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-04-10T13:59:02Z
- Update date including text: 2026-04-10T13:59:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6674",
    "number": "6674",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "S001218",
        "district": "1",
        "firstName": "Melanie",
        "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
        "lastName": "Stansbury",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "CLAIM Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T13:59:02Z",
    "updateDateIncludingText": "2026-04-10T13:59:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:06:20Z",
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
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6674ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6674\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Ms. Stansbury (for herself and Mr. Huffman ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Omnibus Budget Reconciliation Act of 1993 to update provisions related to the hardrock mining claim maintenance fee established under that Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Conserving Lands and Areas Incompatible with Mining Act of 2025 or the CLAIM Act of 2025 .\n#### 2. Hardrock mining claim maintenance fee\nSubtitle B of title X of the Omnibus Budget Reconciliation Act of 1993 ( 30 U.S.C. 28f et seq. ) is amended\u2014\n**(1)**\nby striking Secretary of the Interior each place it appears and inserting Secretary ;\n**(2)**\nin section 10101 ( 30 U.S.C. 28f )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nby striking of $100 and all that follows through the end and inserting per claim or site, respectively, in accordance with the following: ; and\n**(II)**\nby adding at the end the following:\n(A) For a claim or site the majority of which is located within the boundary of a covered area, $1,100. (B) For a claim or site the majority of which is located between 0 and 10 miles from the boundary of a covered area, $1,000. (C) For a claim or site the majority of which is located between 10 and 20 miles from the boundary of a covered area, $700. (D) For a claim or site the majority of which is located between 20 and 30 miles from the boundary of a covered area, $500. (E) For a claim or site the majority of which is located more than 30 miles from the boundary of a covered area, $300. ;\n**(ii)**\nin paragraph (2), by striking the second sentence; and\n**(iii)**\nby adding at the end the following:\n(3) Fee in lieu of assessment work A claim maintenance fee paid in accordance with paragraph (1) or (2) shall be in lieu of the assessment work requirement contained in the Mining Law of 1872 ( 30 U.S.C. 28\u201328e ) and the related filing requirements contained in subsections (a) and (c) of section 314 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1744(a) and (c)). (4) Exemption for small miners Paragraphs (1) and (2) and any assessment work required by the Mining Law of 1872 ( 30 U.S.C. 28 et seq. ) do not apply with respect to a small miner. ; and\n**(B)**\nby striking subsection (d);\n**(3)**\nin section 10105 ( 30 U.S.C. 28j ), by amending subsection (c) to read as follows:\n(c) Fee adjustments (1) Inflation The Secretary shall, not less than once every 5 years after the date of the enactment of the CLAIM Act of 2025 , adjust each fee paid under this section to reflect changes in the Consumer Price Index published by the Bureau of Labor Statistics of the Department of Labor, or more frequently if the Secretary determines an adjustment to be reasonable. (2) Notice The Secretary shall provide each claimant notice of any adjustment made under this subsection not later than July 1 of the year in which the adjustment is made. (3) Applicability A fee adjustment made under this subsection shall begin to apply in the calendar year following the calendar year in which it is made. ; and\n**(4)**\nby adding at the end the following:\n10107. User fees The Secretary may establish and collect from each person subject to the requirements of this subtitle such user fees as may be necessary to reimburse the United States for expenses incurred in the administration of such requirements. 10108. Use of claim maintenance fees (a) In general The Secretary shall use amounts paid to the Secretary pursuant to section 10101(a) to administer the mining laws of the United States. (b) Allocation of excess amounts With respect to a given fiscal year, if amounts paid to the Secretary pursuant to section 10101(a) are in excess of the amount required for the Secretary to administer the mining laws of the United States, the Secretary shall allocate such excess amounts in accordance with the following: (1) 40 percent to the program established by the Secretary under section 40704(a) of the Infrastructure Investment and Jobs Act ( 30 U.S.C. 1245(a) ). (2) 20 percent to the Tribal Historic Preservation Program. (3) 20 percent to the States on the basis of the ratio of the number of patented and unpatented mining claims, mill sites, and tunnel sites located pursuant to the mining laws of the United States located within a State to the total number of patented and unpatented mining claims, mill sites, and tunnel sites located pursuant to the mining laws of the United States. (4) 10 percent to the Land and Water Conservation Fund established under section 200302 of title 54, United States Code, which shall be considered income to the Land and Water Conservation Fund for purposes of section 200302 of that title. (5) 10 percent to the National Parks and Public Land Legacy Restoration Fund established by section 200402(a) of title 54, United States Code. 10109. Definitions In this subtitle: (1) Casual use The term casual use \u2014 (A) means mineral activities that do not ordinarily result in any disturbance of Federal land and resources; (B) includes collection of geochemical, rock, soil, or mineral specimens using handtools, hand panning, or nonmotorized sluicing; and (C) does not include\u2014 (i) the use of mechanized earth-moving equipment, suction dredging, or explosives; (ii) the use of motor vehicles in areas closed to motor vehicles; (iii) the construction of roads or drill pads; or (iv) the use of toxic or hazardous materials. (2) Covered area The term covered area means a\u2014 (A) unit of the National Park System; and (B) national monument designated under section 320301 of title 54, United States Code (commonly known as the Antiquities Act ). (3) Hardrock mineral The term hardrock mineral \u2014 (A) means any mineral that is subject to location under the mining laws of the United States and is not subject to disposition under\u2014 (i) the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ); (ii) the Geothermal Steam Act of 1970 ( 30 U.S.C. 1001 et seq. ); (iii) the Act of July 31, 1947, commonly known as the Materials Act of 1947 ( 30 U.S.C. 601 et seq. ); or (iv) the Mineral Leasing Act for Acquired Lands ( 30 U.S.C. 351 et seq. ); and (B) does not include any mineral that is subject to a restriction against alienation imposed by the United States and is\u2014 (i) held in trust by the United States for any Indian or Indian Tribe; or (ii) owned by any Indian or Indian Tribe. (4) Indian The term Indian has the meaning given the term in section 2 of the Indian Mineral Development Act of 1982 ( 25 U.S.C. 2101 ). (5) Indian Tribe The term Indian Tribe has the meaning given the term in section 2 of the Indian Mineral Development Act of 1982 ( 25 U.S.C. 2101 ). (6) Mineral activities The term mineral activities means any activity carried out on a mining claim, mill site, or tunnel site located pursuant to the mining laws of the United States for, related to, or incidental to, mineral exploration, mining, beneficiation, processing, or reclamation activities for any hardrock mineral. (7) Secretary The term Secretary means the Secretary of the Interior. (8) Small miner (A) In general The term small miner means a person (including all related parties) that\u2014 (i) holds not more than 10 mining claims, mill sites, or tunnel sites, or any combination thereof, on Federal land; (ii) holds or operates a mining claim, mill site, or tunnel site with respect to not more than 200 acres of Federal land; (iii) certifies to the Secretary in writing that, in the preceding calendar year, the person had an annual gross income from mineral production in an amount less than $50,000; and (iv) certifies to the Secretary in writing that the person will use each mining claim, mill site, or tunnel site held or operated by the person only for casual use. (B) Annual gross income For purposes of subparagraph (A)(iii), the dollar amount shall be applied, for a person, to the aggregate of all annual gross income from mineral production under each mining claim, mill site, or tunnel site located pursuant to the mining laws of the United States held by or assigned to such person and all related parties. (C) All related parties For purposes of subparagraphs (A) and (B), with respect to a person, the term all related parties means\u2014 (i) the spouse or qualifying child (as such term is defined in section 152 of the Internal Revenue Code of 1986) of such person; (ii) a person that controls, is controlled by, or is under common control with such person; (iii) a partner of such person; or (iv) a person that owns at least 10 percent of the voting shares of such person. (D) Control For purposes of subparagraph (C), the term control means having the ability, directly or indirectly, to determine (without regard to whether exercised through 1 or more corporate structures) the manner in which an entity conducts mineral activities, through any means, including\u2014 (i) an ownership interest; (ii) the authority to commit the real or financial assets of the entity; (iii) a position as a director, officer, or partner of the entity; or (iv) a contractual arrangement. .",
      "versionDate": "2025-12-11",
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
        "name": "Energy",
        "updateDate": "2026-04-10T13:59:02Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6674ih.xml"
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
      "title": "CLAIM Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLAIM Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Conserving Lands and Areas Incompatible with Mining Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Budget Reconciliation Act of 1993 to update provisions related to the hardrock mining claim maintenance fee established under that Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:20Z"
    }
  ]
}
```
