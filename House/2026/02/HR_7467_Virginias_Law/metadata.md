# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7467?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7467
- Title: Virginia’s Law
- Congress: 119
- Bill type: HR
- Bill number: 7467
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-05-27T08:05:55Z
- Update date including text: 2026-05-27T08:05:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7467",
    "number": "7467",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Virginia\u2019s Law",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:55Z",
    "updateDateIncludingText": "2026-05-27T08:05:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:02:30Z",
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
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "MD"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7467ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7467\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Ms. Leger Fernandez introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to create a civil cause of action for certain crimes and to eliminate the statute of limitations for civil actions relating to certain crimes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Virginia\u2019s Law .\n#### 2. Civil remedies\n##### (a) Sexual abuse\n**(1) In general**\nChapter 109A of title 18, United States Code, is amended by adding at the end the following:\n2249. Civil remedy (a) An individual who is a victim of a violation of this chapter may bring a civil action against the perpetrator (or whoever knowingly benefits, or attempts or conspires to benefit, financially or by receiving anything of value from participation in a venture which that person knew or should have known has engaged in an act in violation of this chapter) in any district court of the United States that has jurisdiction to hear a criminal prosecution arising out of the same conduct or occurrence and may recover damages and reasonable attorneys fees. (b) (1) Any civil action filed under subsection (a) shall be stayed during the pendency of any criminal action arising out of the same occurrence in which the claimant is the victim. (2) In this subsection, the term criminal action includes investigation and prosecution and is pending until final adjudication in the trial court. (c) (1) Subject to paragraph (2), no action may be maintained under subsection (a) unless it is commenced not later than the later of\u2014 (A) 10 years after the cause of action arose; or (B) 10 years after the victim reaches 18 years of age, if the victim was a minor at the time of the alleged offense. (2) There shall be no time limit for the filing of a complaint commencing an action under this section relating to an alleged violation of section 2241, 2242, or 2243. .\n**(2) Clerical amendment**\nThe table of sections for chapter 109A of title 18, United States Code, is amended by adding at the end the following:\n2249. Civil remedy. .\n##### (b) Transportation for illegal sexual activity and related crimes\n**(1) In general**\nChapter 117 of title 18, United States Code, is amended by adding at the end the following:\n2430. Civil remedy (a) An individual who is a victim of a violation of this chapter may bring a civil action against the perpetrator (or whoever knowingly benefits, or attempts or conspires to benefit, financially or by receiving anything of value from participation in a venture which that person knew or should have known has engaged in an act in violation of this chapter) in any district court of the United States that has jurisdiction to hear a criminal prosecution arising out of the same conduct or occurrence and may recover damages and reasonable attorneys fees. (b) (1) Any civil action filed under subsection (a) shall be stayed during the pendency of any criminal action arising out of the same occurrence in which the claimant is the victim. (2) For purposes of this subsection, a criminal action \u2014 (A) includes investigation and prosecution; and (B) is pending until final adjudication in the trial court. (c) (1) Except as provided in paragraph (2), no action may be maintained under subsection (a) unless it is commenced not later than the later of\u2014 (A) 10 years after the cause of action arose; or (B) 10 years after the victim reaches 18 years of age, if the victim was a minor at the time of the alleged offense. (2) There shall be no time limit for the filing of a complaint commencing an action under this section relating to an alleged violation of section 2421, 2422, or 2423. .\n**(2) Clerical amendment**\nThe table of sections for chapter 117 of title 18, United States Code, is amended by adding at the end the following:\n2430. Civil remedy. .\n#### 3. Elimination of statute of limitations\nSection 1595 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking an appropriate district court of the United States and inserting any district court of the United States that has jurisdiction to hear a criminal prosecution arising out of the same conduct or occurrence ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and adjusting the margins accordingly;\n**(B)**\nin the matter preceding subparagraph (B), as so redesignated, by striking (c) No action and inserting the following:\n(c) (1) Subject to paragraph (2), no action ; and\n**(C)**\nby adding at the end the following:\n(2) There shall be no time limit for the filing of a complaint commencing an action under this section relating to an alleged violation of section 1589, 1590, or 1591. .\n#### 4. Applicability\n##### (a) In general\nSubject to subsection (b), this Act and the amendments made by this Act shall apply to\u2014\n**(1)**\nany claim or action that, as of the date of enactment of this Act, would not have been barred under section 1595(c) of title 18, United States Code, as in effect on the day before the date of enactment of this Act; and\n**(2)**\nany claim or action arising on or after the date of enactment of this Act.\n##### (b) 1-Year look back period\n**(1) Covered action defined**\nIn this subsection, the term covered action \u2014\n**(A)**\nmeans\u2014\n**(i)**\na civil action that could have been brought on the day before the date of enactment of this Act under section 2249 or 2430 of title 18, United States Code, as added by this Act, if that section had been in effect on that day; and\n**(ii)**\na civil action under section 1595 of title 18, United States Code, relating to an alleged violation of section 1589, 1590, or 1591 of that title that was barred under section 1595(c) of that title as in effect on the day before the date of enactment of this Act; and\n**(B)**\nincludes a civil action described in subparagraph (A)(ii) that was dismissed before the date of enactment of this Act on the basis of the time limit imposed on commencing an action under section 1595(c) of title 18, United States Code, as in effect on the day before the date of enactment of this Act.\n**(2) Filing period**\nNotwithstanding any other provision of law, a covered action may be commenced during the 1-year period beginning on the date of enactment of this Act.",
      "versionDate": "2026-02-10",
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
        "actionDate": "2026-02-10",
        "text": "Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S554-555; text: CR S555)"
      },
      "number": "3815",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Virginia's Law",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-27T15:16:49Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7467ih.xml"
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
      "title": "Virginia\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Virginia\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to create a civil cause of action for certain crimes and to eliminate the statute of limitations for civil actions relating to certain crimes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:25Z"
    }
  ]
}
```
