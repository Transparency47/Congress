# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1934?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1934
- Title: ProTECT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1934
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-03-21T16:33:36Z
- Update date including text: 2025-03-21T16:33:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1934",
    "number": "1934",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "L000582",
        "district": "36",
        "firstName": "Ted",
        "fullName": "Rep. Lieu, Ted [D-CA-36]",
        "lastName": "Lieu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "ProTECT Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-21T16:33:36Z",
    "updateDateIncludingText": "2025-03-21T16:33:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:01:20Z",
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
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-06",
      "state": "GA"
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
      "sponsorshipDate": "2025-03-06",
      "state": "DC"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NV"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "FL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1934ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1934\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Lieu (for himself, Mr. Nadler , Mr. Johnson of Georgia , Ms. Norton , Mr. Krishnamoorthi , Ms. Titus , Mr. Soto , and Mr. Huffman ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Endangered Species Act of 1973 to prohibit the taking for a trophy of any endangered or threatened species of fish or wildlife in the United States and the importation of endangered and threatened species trophies into the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prohibiting Threatened and Endangered Creature Trophies Act of 2025 or the ProTECT Act of 2025 .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nTrophy hunting of imperiled species undermines efforts to conserve wildlife populations because trophy hunters routinely target the biggest, strongest males, and removing those individuals from the population can decrease genetic variation, decrease reproduction, alter social structures, increase infanticide, and cause unnatural evolutionary impacts.\n**(2)**\nWhen trophy hunting of imperiled species is sanctioned, poaching activity increases, further threatening the survival of wildlife populations.\n**(3)**\nLegal trade in wildlife parts and products can provide cover for markets for illegal trade in wildlife products, which is worth up to $20,000,000,000 annually and run by professional criminal networks linked to other transnational organized criminal activities, including trafficking in narcotics, weapons, and humans.\n**(4)**\nWhile the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) currently prohibits the take and import of species listed under that Act as endangered species, it does not automatically extend those protections to species listed as threatened species.\n#### 3. Prohibitions regarding taking and importing of endangered species and threatened species trophies\n##### (a) Prohibition of taking or importing\nSection 9 of the Endangered Species Act of 1973 ( 16 U.S.C. 1538 ) is amended by adding at the end the following:\n(h) Trophies It is unlawful for any person subject to the jurisdiction of the United States\u2014 (1) to take for a trophy within the United States or the territorial sea of the United States any species of fish or wildlife listed under section 4 as a threatened species; or (2) to import into the United States any trophy of any species of fish or wildlife listed under section 4 as a threatened species. .\n##### (b) Prohibition of permits\nSection 10(a) of the Endangered Species Act of 1973 ( 16 U.S.C. 1539(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking The Secretary may permit and inserting Except as otherwise provided in this subsection, the Secretary may permit ; and\n**(2)**\nby adding at the end the following:\n(3) The Secretary may not permit or otherwise allow\u2014 (A) taking for a trophy any species of fish or wildlife listed under section 4; or (B) importing into the United States any trophy of any species of fish or wildlife listed under section 4, notwithstanding section 9(b). .\n##### (c) Antiques\nSection 10(h)(1) of the Endangered Species Act of 1973 ( 16 U.S.C. 1539(h)(1) ) is amended by striking Sections 4(d), 9(a), and 9(c) do not apply and inserting Sections 4(d), 9(a), 9(c), and 9(h)(2) do not apply .\n##### (d) Definition\nSection 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 ) is amended\u2014\n**(1)**\nby redesignating paragraph (21) as paragraph (22); and\n**(2)**\nby inserting after paragraph (20) the following:\n(21) The term trophy means a whole dead animal, or a readily recognizable part or derivative of an animal, that\u2014 (A) is raw, processed, or manufactured; and (B) was obtained under a hunting license or other authorization issued by any State, foreign government, or private landowner. .",
      "versionDate": "2025-03-06",
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
        "name": "Environmental Protection",
        "updateDate": "2025-03-21T16:33:36Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1934ih.xml"
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
      "title": "ProTECT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ProTECT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prohibiting Threatened and Endangered Creature Trophies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Endangered Species Act of 1973 to prohibit the taking for a trophy of any endangered or threatened species of fish or wildlife in the United States and the importation of endangered and threatened species trophies into the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:30Z"
    }
  ]
}
```
