# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3456?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3456
- Title: CHER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3456
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-06-20T13:55:07Z
- Update date including text: 2025-06-20T13:55:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3456",
    "number": "3456",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "CHER Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-20T13:55:07Z",
    "updateDateIncludingText": "2025-06-20T13:55:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3456ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3456\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Ms. Malliotakis introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Animal Welfare Act to prohibit keeping elephants in captivity at zoological parks or safari parks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Captivity of Helpless Elephants Reduction Act of 2025 or the CHER Act of 2025 .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nElephants live in a matriarchal hierarchy where a lead female leads a large herd in the wild and migrates, traveling hundreds of miles every year. African and Asian elephants have been demonstrated to possess, amongst other things, intentional communication and learning, memory, and categorization abilities. An Emory University experiment showed that a female elephant seemed to recognize herself in a mirror, a result attributed to self-awareness only seen otherwise in humans, dolphins, and chimpanzees.\n**(2)**\nCaptivity does not provide for the needs of normal elephant behavior and reproduction. As a result, captive elephants suffer both physical and emotional trauma including hernias, arthritis, mental degradation, and high calf mortality. The average lifespan of a captive elephant is 17 years; in the wild, elephants can live for 50 years or more.\n**(3)**\nIt is estimated that the cost of caring for an elephant in captivity can be up to $100,000 per year. In 2004, the Detroit Zoo became the first major American zoo to shut down its elephant exhibit on ethical grounds. In 2006, the Bronx Zoo announced that it would close its exhibit once its three elephants died. Since the early 1990s, more than 22 zoos have shut down their elephant exhibits or announced that they were phasing them out, including those in Seattle, San Francisco, and Chicago.\n**(4)**\nThe United Kingdom phased out all circuses featuring wild animal performances by 2020 and announced its intention to ban the captivity of elephants in zoos and safari parks. Dozens of other countries around the world have similar prohibitions, including Austria, Greece, Israel, Mexico, Peru, and Singapore. India bans the keeping of elephants in circuses and zoos.\n##### (b) Purpose\nThe purpose of this Act is to ban the display, husbandry, and breeding of African elephants and Asian elephants in zoological parks and safari parks in the United States and transfer existing African elephants and Asian elephants in zoological parks and safari parks to authorized wildlife sanctuaries.\n#### 3. Prohibition on elephant captivity\nThe Animal Welfare Act ( 7 U.S.C. 2131 et seq. ) is amended by adding at the end the following:\n30. Prohibition on elephant captivity (a) In general An exhibitor that is a safari park or zoological park may not exhibit, house, manage, or breed an African elephant or an Asian elephant after the date that is 1 year after the date of the enactment of this section, except to complete a transfer of an African elephant or an Asian elephant pursuant to subsection (b). (b) Transfer to authorized wildlife sanctuaries The Secretary shall require each exhibitor that is a safari park or zoological park that exhibits, houses, manages, or breeds an African elephant or an Asian elephant as of the date of the enactment of this section to transfer such African elephant or Asian elephant to an authorized wildlife sanctuary not later than 3 years after the date of the enactment of this section. (c) Definitions In this section: (1) African elephant The term African elephant has the meaning given the term in section 2305 of the African Elephant Conservation Act ( 16 U.S.C. 4244 ). (2) Authorized wildlife sanctuary The term authorized wildlife sanctuary means a nonprofit facility that\u2014 (A) is accredited by the Global Federation of Animal Sanctuaries or a similar body; (B) is dedicated to the lifelong care of elephants; (C) does not\u2014 (i) breed animals; (ii) exhibit animals for profit; or (iii) use animals for public entertainment; and (D) meets the standards promulgated under this Act for\u2014 (i) space; (ii) veterinary care; and (iii) naturalistic environments. (3) Safari park The term safari park means a facility, whether publicly or privately owned, that\u2014 (A) houses animals in large enclosures for public viewing; and (B) allows visitors to drive through or observe animals in a simulated natural environment. (4) Zoological park The term zoological park \u2014 (A) means a facility, whether publicly or privately owned, that exhibits live animals to the public for educational or entertainment purposes; and (B) includes zoos and aquariums. .\n#### 4. Implementation and support\n##### (a) Feasibility study\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall conduct a study to assess the feasibility of transferring African elephants and Asian elephants to authorized wildlife sanctuaries, including capacity, costs, and logistics.\n##### (b) Grant program\nThe Secretary may establish a grant program to support the accommodation by authorized wildlife sanctuaries of African elephants and Asian elephants transferred to such authorized wildlife sanctuaries pursuant to section 30 of the Animal Welfare Act (as added by this Act).\n##### (c) Public education\nThe Secretary shall develop materials to educate the public about the welfare benefits of prohibiting the captivity of African elephants and Asian elephants.\n##### (d) Definitions\nIn this section:\n**(1) African elephant**\nThe term African elephant has the meaning given the term in section 2305 of the African Elephant Conservation Act ( 16 U.S.C. 4244 ).\n**(2) Authorized wildlife sanctuary**\nThe term authorized wildlife sanctuary has the meaning given the term in section 30 of the Animal Welfare Act (as added by this Act).\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.",
      "versionDate": "2025-05-15",
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
        "updateDate": "2025-06-20T13:55:07Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3456ih.xml"
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
      "title": "CHER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Captivity of Helpless Elephants Reduction Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Animal Welfare Act to prohibit keeping elephants in captivity at zoological parks or safari parks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:20Z"
    }
  ]
}
```
