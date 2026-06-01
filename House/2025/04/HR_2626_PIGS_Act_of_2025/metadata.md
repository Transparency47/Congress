# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2626?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2626
- Title: PIGS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2626
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2025-06-11T20:15:06Z
- Update date including text: 2025-06-11T20:15:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2626",
    "number": "2626",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "E000299",
        "district": "16",
        "firstName": "Veronica",
        "fullName": "Rep. Escobar, Veronica [D-TX-16]",
        "lastName": "Escobar",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "PIGS Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-11T20:15:06Z",
    "updateDateIncludingText": "2025-06-11T20:15:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:15:00Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2626ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2626\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Ms. Escobar (for herself and Ms. Norton ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Animal Welfare Act to prohibit the confinement of pregnant pigs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pigs In Gestation Stalls Act of 2025 or the PIGS Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nIntensive confinement of pigs is a significant animal welfare issue, causing physical problems and psychological anguish for the animals.\n**(2)**\nDozens of major food retailers and more than 10 States have taken action to phase out the use of intensive confinement for pigs, reflecting the will and concerns of the public.\n**(3)**\nAt least two States have adopted policies to forbid the sale of pork from factory farms that use gestation crates, with that policy predicated on human health and animal welfare concerns.\n**(4)**\nAs more consumers turn away from purchasing pork products derived from intensive confinement practices, the pork industry will be better aligned with its customers by ending these unpopular and inhumane housing methods.\n#### 3. Prohibition on confining breeding pigs\n##### (a) In general\nThe Animal Welfare Act ( 7 U.S.C. 2131 et seq. ) is amended by adding at the end the following:\n30. Prohibition on confining breeding pigs (a) Prohibition (1) In general It shall be unlawful for a person to cause any breeding pig to be confined in\u2014 (A) such a manner that prevents the pig from lying down, standing up, or turning around\u2014 (i) in a complete circle without any impediment, including a tether; and (ii) without touching the side of an enclosure or another animal; and (B) beginning on December 31, 2025, a space with less than 24 square feet of usable floorspace per pig, as calculated under paragraph (3). (2) Exceptions The Secretary shall not, in applying paragraph (1), consider a breeding pig to be confined in a cruel manner if such confinement occurs during\u2014 (A) transportation; (B) examination, testing, treatment, or an operation conducted for veterinary purposes, but only if performed by or under the direct supervision of a licensed veterinarian; (C) the five-day period before the pig\u2019s expected date of farrowing; and (D) slaughter conducted in accordance with the Humane Methods of Slaughter Act ( 7 U.S.C. 1901 et seq. ). (3) Calculation of usable floorspace For purposes of paragraph (1)(B), the total square footage of floorspace provided to each breeding pig in an enclosure shall be determined by dividing\u2014 (A) the total square footage of floorspace provided to all the animals in such enclosure; by (B) the number of animals in that enclosure. (b) Penalties For the purpose of administering and enforcing this section, the authorities provided under sections 10414 and 10415 of the Animal Health Protection Act (7 U.S.C. 8313 and 8314) shall apply to this section in a similar manner as those sections apply to the Animal Health Protection Act ( 7 U.S.C. 8301 et seq. ). Any person that violates the prohibition under subsection (a) shall be subject to penalties provided in such section 10414. (c) No preemption Nothing in this section preempts any State or local laws, regulations, orders, or other requirements with respect to animal welfare that are identical to, or are in addition to, the requirements of this section. (d) Rule of construction Nothing in this section shall be construed as limiting the authority of the Secretary under this Act or another Federal law to protect animal welfare. (e) Severability If this section is held unconstitutional as to some provisions or circumstances, it shall remain in force as to the remaining provisions and other circumstances. (f) Financial assistance (1) In general The Secretary shall establish a program under which the Secretary will provide financial assistance to pig producers to assist such producers in complying with the requirements of this section. (2) Priority The Secretary shall allocate funds made available under paragraph (3) among pig producers in a manner that prioritizes independent pig producers. (3) Funding The Secretary shall amend the order in effect as of the date of the enactment of this section under section 1616(c) of the Pork Promotion, Research, and Consumer Information Act of 1985 ( 7 U.S.C. 4805(c) ), to direct the National Pork Board, notwithstanding section 1620(c) of such Act ( 7 U.S.C. 4809(c) ), to set aside not less than $10,000,000 of the funds collected from assessments made under such Act for the first fiscal year that begins after the date of the enactment of this section and the following fiscal year to provide assistance to pig producers, as described in paragraph (1). (g) Definitions In this section: (1) The term breeding pig means any female pig that is\u2014 (A) kept for the purpose of commercial breeding who is six months of age or older; or (B) pregnant. (2) The term enclosure means any cage, crate or other enclosure in which a pig is kept, including, a gestation crate. (3) The term pig means any animal of the porcine species. (4) The term independent pig producer means a pig producer who owns their own pigs and is not contracted to raise pigs that belong to another entity. .\n##### (b) Applicability\nThe amendment made by this section shall apply beginning on the date that is one year after the date of the enactment of this Act.",
      "versionDate": "2025-04-03",
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
        "name": "Animals",
        "updateDate": "2025-06-11T20:15:06Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2626ih.xml"
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
      "title": "PIGS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PIGS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pigs In Gestation Stalls Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Animal Welfare Act to prohibit the confinement of pregnant pigs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T05:48:24Z"
    }
  ]
}
```
