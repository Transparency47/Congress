# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8962?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8962
- Title: PERFECT Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8962
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-28T22:30:28Z
- Update date including text: 2026-05-28T22:30:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-05-21: Introduced in House

## Actions

- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8962",
    "number": "8962",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "PERFECT Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-28T22:30:28Z",
    "updateDateIncludingText": "2026-05-28T22:30:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-21",
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
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-21",
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
          "date": "2026-05-21T14:03:50Z",
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
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "NC"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8962ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8962\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2026 Mr. Davidson (for himself, Mr. Harrigan , Mr. Khanna , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to direct the Secretary of Defense to publish a list of dietary supplement ingredients prohibited for use by members of the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Enlisted and Recruits from Excessive and Catastrophic Trials Act of 2026 or the PERFECT Act of 2026 .\n#### 2. Prohibited dietary supplement ingredients and performance-enhancing substances\n##### (a) Prohibition\nChapter 49 of title 10, United States Code, is amended by inserting after section 978 the following new section:\n978a. Prohibited dietary supplement ingredients and performance-enhancing substances (a) Prohibited ingredient and substance lists The Secretary shall publish and, not less frequently than once every 90 days, shall update a list of\u2014 (1) dietary supplement ingredients prohibited for use by members of the armed forces; and (2) performance-enhancing substances prohibited for use by members of the armed forces. (b) Required formats The Secretary shall publish the list under subsection (a)\u2014 (1) on an internet website where such list may be viewed in full without use of a search function; (2) in a searchable database; and (3) in a digital file that may be downloaded from such internet website in a common format. (c) Commanding officer may elect not to discipline The commanding officer of a member of the armed forces who possesses or uses a dietary supplement containing an ingredient (other than a substance included in the schedule under section 202 of the Controlled Substances Act ( 21 U.S.C. 812 )) appearing on the list under subsection (a)(1)\u2014 (1) may elect not to subject such member to discipline if\u2014 (A) such possession or use is the first disciplinary offense committed by such member; (B) such commanding officer determines that such member satisfies the good faith standard under subsection (e); and (C) such member agrees to participate in education, counseling, or drug testing in lieu of discipline; and (2) may elect not to subject such member to administrative separation. (d) Possession of prohibited ingredient not drug abuse Notwithstanding any other provision of law, possession of a dietary supplement containing an ingredient (other than a substance included in the schedule under section 202 of the Controlled Substances Act ( 21 U.S.C. 812 )) appearing on the list under subsection (a)(1) shall not constitute drug abuse for purposes of this title. (e) Good faith standard A member of the armed forces satisfies the good faith standard under this subsection if such member\u2014 (1) possesses or uses a dietary supplement containing an ingredient (other than a substance included in the schedule under section 202 of the Controlled Substances Act ( 21 U.S.C. 812 )) appearing on the list under subsection (a)(1) without actual knowledge that such dietary supplement contains such ingredient; (2) purchases such supplement from a retail facility affiliated with the Department of Defense; (3) reasonably relies, prior to purchasing or using such supplement, on a search of the list under subsection (a)(1) that fails to identify such ingredient as prohibited under subsection (a)(1), including due to a misspelling or variation in the name of such ingredient on such list; or (4) otherwise demonstrates a reasonable belief that such supplement does not contain such ingredient. .\n##### (b) Secretary to update Department of Defense Instruction\nNot later than 120 days after the date of the enactment of this Act, the Secretary of Defense, acting through the Under Secretary for Personnel and Readiness, shall revise Department of Defense Instruction 6130.06 pursuant to section 978a of title 10, United States Code, as added by subsection (a).\n##### (c) Secretary to update Operation Supplement Safety internet website\nNot later than one year after the date of the enactment of this Act, the Secretary shall\u2014\n**(1)**\nupdate the Operation Supplement Safety internet website to enhance functionality for\u2014\n**(A)**\nvendors of dietary supplements; and\n**(B)**\nmembers of the Armed Forces; and\n**(2)**\nreview possible improvements to such internet website, including with respect to\u2014\n**(A)**\nsearch tools that employ\u2014\n**(i)**\nautofill functionality; and\n**(ii)**\nautocorrect functionality;\n**(B)**\nartificial intelligence tools that can\u2014\n**(i)**\nscan product labels; and\n**(ii)**\nsearch such internet website for information on the ingredients found on such labels; and\n**(C)**\ncapacity to allow a user to register to receive a notification when a dietary supplement ingredient is added to the list under section 978a(a)(1) of title 10, United States Code, as added by subsection (a).\n##### (d) Secretary to review dietary supplement safety education opportunities\nNot later than one year after the date of the enactment of this Act, the Secretary shall review opportunities for incorporating into existing training programs for members of the Armed Forces education concerning\u2014\n**(1)**\ndietary supplement safety; and\n**(2)**\nthe list under section 978a(a) of title 10, United States Code, as added by subsection (a).\n##### (e) Reports\n**(1) Initial implementation report**\nNot later than 120 days after the date of the enactment of this Act, the Secretary shall submit to the Committees on Armed Services of the House of Representatives and the Senate a report describing efforts made to ensure that retail facilities affiliated with the Department of Defense do not sell any products containing an ingredient appearing on the list under section 978a(a) of title 10, United States Code, as added by subsection (a).\n**(2) Final implementation report**\nNot later than two years after the date of the enactment of this Act, the Secretary shall submit to the Committees on Armed Services of the House of Representatives and the Senate a report describing steps taken to implement section 978a of title 10, United States Code, as added by subsection (a).\n**(3) Annual reports**\nNot later than one year after the date of the enactment of this Act, and annually thereafter for a period of five years, the Secretary shall submit to the Committees on Armed Services of the House of Representatives and the Senate a report\u2014\n**(A)**\nlisting, for the one-year period ending on the date on which such report is submitted\u2014\n**(i)**\nthe total number of administrative separation actions initiated for possession or use of a dietary supplement containing an ingredient appearing on the list under section 978a(a)(1) of title 10, United States Code, as added by subsection (a), disaggregated by\u2014\n**(I)**\narmed force;\n**(II)**\npay grade;\n**(III)**\ncharacterization of discharge sought;\n**(IV)**\nwhether the member subject to the administrative separation action contested such action; and\n**(V)**\noutcome; and\n**(ii)**\nthe number of commanding officers who elected not to subject a member of the Armed Forces to discipline under section 978a(c) of such title; and\n**(B)**\nassessing the effectiveness of efforts to provide education relating to dietary supplement safety to members of the Armed Forces.",
      "versionDate": "2026-05-21",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-28T22:30:28Z"
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
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8962ih.xml"
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
      "title": "PERFECT Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PERFECT Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Enlisted and Recruits from Excessive and Catastrophic Trials Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to direct the Secretary of Defense to publish a list of dietary supplement ingredients prohibited for use by members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:37Z"
    }
  ]
}
```
