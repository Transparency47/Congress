# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7861?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7861
- Title: Care Over Profits Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7861
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-02T18:44:32Z
- Update date including text: 2026-04-02T18:44:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7861",
    "number": "7861",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Care Over Profits Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-02T18:44:32Z",
    "updateDateIncludingText": "2026-04-02T18:44:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7861ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7861\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Barrett (for himself and Mr. Riley of New York ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXVII of the Public Health Service Act and the Patient Protection and Affordable Care Act to provide for certain reforms with respect to medical loss ratios and reducing fraudulent enrollment in qualified health plans.\n#### 1. Short title\nThis Act may be cited as the Care Over Profits Act of 2026 .\n#### 2. Increasing medical loss ratio for health insurance coverage offered in small group and individual markets\n##### (a) In general\nSection 2718(b)(1)(A)(ii) of the Public Health Service Act ( 42 U.S.C. 300gg\u201318(b)(1)(A)(ii) ) is amended by striking 80 each place it appears and inserting 85 .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to plan years beginning on or after January 1, 2026.\n#### 3. Imposing penalties on agents and brokers for certain violations with respect to enrollment in a qualified health plan offered through an Exchange\n##### (a) In general\nSection 1411(h)(1) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18081(h)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby redesignating clause (ii) as clause (iv);\n**(B)**\nin clause (i)\u2014\n**(i)**\nby striking If\u2014 and all that follows through such person and inserting If any person (other than an agent or broker) fails to provide correct information under subsection (b) and such failure is attributable to negligence or disregard of any rules or regulations of the Secretary, such person ; and\n**(ii)**\nin the second sentence, by striking For purposes and inserting the following:\n(iii) Definitions of negligence, disregard For purposes ;\n**(C)**\nby inserting after clause (i) the following:\n(ii) Civil penalties for certain violations by agents or brokers If any agent or broker fails to provide correct information under subsection (b), or other information as part of an application for enrollment in a qualified health plan offered through an Exchange, as specified by the Secretary, and such failure is attributable to negligence or disregard of any rules or regulations of the Secretary, such agent or broker shall be subject, in addition to any other penalties that may be prescribed by law, including subparagraph (C), to a civil penalty of not less than $10,000 and not more than $50,000 with respect to each individual who is the subject of an application for which such incorrect information is provided. ; and\n**(D)**\nin clause (iv) (as so redesignated), by inserting or (ii) after clause (i) ;\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nby inserting including subparagraph (C), after law, ;\n**(B)**\nby striking Any person and inserting the following:\n(i) In general Any person ; and\n**(C)**\nby adding at the end the following:\n(ii) Civil penalties for knowing and willful violations by agents or brokers (I) In general Any agent or broker who knowingly and willfully provides false or fraudulent information under subsection (b), or other false or fraudulent information as part of an application for enrollment in a qualified health plan offered through an Exchange, as specified by the Secretary, shall be subject, in addition to any other penalties that may be prescribed by law, including subparagraph (C), to a civil monetary penalty of not more than $200,000 with respect to each individual who is the subject of an application for which such false or fraudulent information is provided. (II) Procedure The provisions of section 1128A of the Social Security Act (other than subsections (a) and (b) of such section) shall apply to a civil monetary penalty under subclause (I) in the same manner as such provisions apply to a penalty or proceeding under section 1128A of the Social Security Act. ; and\n**(3)**\nby adding at the end the following:\n(C) Criminal penalties Any agent or broker who knowingly and willfully provides false or fraudulent information under subsection (b), or other false or fraudulent information as part of an application for enrollment in a qualified health plan offered through an Exchange, as specified by the Secretary, shall be fined under title 18, United States Code, imprisoned for not more than 10 years, or both. .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to applications for enrollment in a qualified health plan offered through an Exchange for plan years beginning on or after January 1, 2027.",
      "versionDate": "2026-03-09",
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
        "name": "Health",
        "updateDate": "2026-04-02T18:44:32Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7861ih.xml"
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
      "title": "Care Over Profits Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T03:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Care Over Profits Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXVII of the Public Health Service Act and the Patient Protection and Affordable Care Act to provide for certain reforms with respect to medical loss ratios and reducing fraudulent enrollment in qualified health plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T03:03:22Z"
    }
  ]
}
```
