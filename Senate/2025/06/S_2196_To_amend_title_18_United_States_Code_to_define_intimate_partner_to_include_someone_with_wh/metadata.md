# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2196?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2196
- Title: Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2196
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2026-05-18T19:27:58Z
- Update date including text: 2026-05-18T19:27:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2196",
    "number": "2196",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025",
    "type": "S",
    "updateDate": "2026-05-18T19:27:58Z",
    "updateDateIncludingText": "2026-05-18T19:27:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-06-26T21:38:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "VA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "VT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-26",
      "state": "VT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "HI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "MD"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "MN"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "RI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "MD"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NH"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "CA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2196is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2196\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Ms. Klobuchar (for herself, Mr. Blumenthal , Mr. Kaine , Mr. Welch , Mr. Durbin , Mr. Sanders , Mr. Markey , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to define intimate partner to include someone with whom there is or was a dating relationship, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025 .\n#### 2. Addressing intimate partner violence\n##### (a) Inclusion of current and former dating partners in definition of intimate partner\nSection 921(a) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (32)\u2014\n**(A)**\nby striking and an individual and inserting an individual ; and\n**(B)**\nby inserting before the period at the end the following: , an individual who is or was in a dating relationship with the person, or any other individual similarly situated to a spouse, including an individual who is protected by the domestic or family violence laws of the State or Tribal jurisdiction in which the abuse occurred or the victim resides ;\n**(2)**\nby striking paragraph (37)(A) and inserting the following:\n(37) (A) The term dating relationship means a relationship between individuals who have or have had, or in the case of a misdemeanor crime of domestic violence have or have recently had, a continuing serious relationship of a romantic or intimate nature. ; and\n**(3)**\nin paragraph (37)(C), by striking dating relationship and inserting continuing serious relationship .\n##### (b) Inclusion of dating partners\u2019 children in definition of misdemeanor crime of domestic violence\nSection 921(a)(33)(A)(ii) of title 18, United States Code, is amended\u2014\n**(1)**\nby striking victim, or by a person and inserting victim, by a person ; and\n**(2)**\nby inserting , or by a person who has a current or recent former dating relationship with the parent, guardian, or person similarly situated to a parent or guardian of the victim before the period at the end.\n##### (c) New prohibitor for misdemeanor crimes of stalking\nChapter 44 of title 18, United States Code, is amended\u2014\n**(1)**\nin section 921(a), by adding at the end the following:\n(39) (A) Except as provided in subparagraphs (B) and (C), the term misdemeanor crime of stalking means an offense that\u2014 (i) is a misdemeanor under Federal, State, Tribal, or local law; and (ii) has as an element a course of harassment, intimidation, or surveillance that\u2014 (I) places a person in reasonable fear of actual harm to the health or safety of\u2014 (aa) that person; (bb) an immediate family member (as defined in section 115) of that person; (cc) an individual who shares or has shared a residence with that person, without regard to whether the individual is related to that person; (dd) an intimate partner of that person; or (ee) the pet, service animal, or emotional support animal (as those terms are defined in section 2266) of that person; or (II) causes, attempts to cause, or would reasonably be expected to cause emotional distress to a person described in item (aa), (bb), (cc), or (dd) of subclause (I). (B) A person shall not be considered to have been convicted of such an offense for purposes of this chapter, unless\u2014 (i) the person was represented by counsel in the case, or knowingly and intelligently waived the right to counsel in the case; and (ii) in the case of a prosecution for an offense described in this paragraph for which a person was entitled to a jury trial in the jurisdiction in which the case was tried, either\u2014 (I) the case was tried by a jury; or (II) the person knowingly and intelligently waived the right to have the case tried by a jury, by guilty plea or otherwise. (C) A person shall not be considered to have been convicted of such an offense for purposes of this chapter if the conviction has been expunged or set aside, or is an offense for which the person has been pardoned or has had civil rights restored (if the law of the applicable jurisdiction provides for the loss of civil rights under such an offense) unless the pardon, expungement, or restoration of civil rights expressly provides that the person may not ship, transport, possess, or receive firearms. ; and\n**(2)**\nin section 922\u2014\n**(A)**\nin subsection (d)\u2014\n**(i)**\nby redesignating paragraphs (10) and (11) as paragraphs (11) and (12), respectively;\n**(ii)**\nby inserting after paragraph (9) the following:\n(10) has been convicted in any court of a misdemeanor crime of stalking; ; and\n**(iii)**\nin paragraph (12), as so redesignated, by striking (10) and inserting (11) ; and\n**(B)**\nin subsection (g)\u2014\n**(i)**\nin paragraph (8), by striking or at the end;\n**(ii)**\nin paragraph (9), by striking the comma at the end and inserting ; or ; and\n**(iii)**\nby inserting after paragraph (9) the following:\n(10) has been convicted in any court of a misdemeanor crime of stalking, .",
      "versionDate": "2025-06-26",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-06-26",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4166",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-07-25T12:11:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-26",
    "originChamber": "Senate",
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
          "measure-id": "id119s2196",
          "measure-number": "2196",
          "measure-type": "s",
          "orig-publish-date": "2025-06-26",
          "originChamber": "SENATE",
          "update-date": "2026-05-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2196v00",
            "update-date": "2026-05-18"
          },
          "action-date": "2025-06-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025</strong></p><p>This bill extends federal restrictions on the receipt, possession, shipment, and transportation of firearms and ammunition to new types of stalking and domestic violence offenders.</p><p>Specifically, the bill extends federal firearms-related restrictions to individuals who are convicted of a misdemeanor crime of stalking. The term <em>misdemeanor crime of stalking</em> means a federal, state, tribal, or local offense involving harassment, intimidation, or surveillance that (1) causes emotional distress; or (2) places a person in reasonable fear of harm to themselves, an immediate family member, a current or former cohabitant, an intimate partner, or a pet.</p><p>Additionally, the bill extends federal firearms-related restrictions to individuals who are subject to a domestic violence protection order that restrains them from harassing, stalking, or threatening a current or former dating partner (regardless of when the relationship occurred) or an individual similarly situated to a spouse. Currently, the restrictions only apply if the domestic violence protection order restrains the individual from harassing, stalking, or threatening a co-parent, a current or former spouse, or a current or former cohabitant.</p><p>Finally, the bill extends federal firearms-related restrictions to individuals who commit a misdemeanor crime of domestic violence against the child of a current or recent former dating partner. Currently, the restrictions only apply if the offense is committed against a current or recent former dating partner.</p>"
        },
        "title": "Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2196.xml",
    "summary": {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025</strong></p><p>This bill extends federal restrictions on the receipt, possession, shipment, and transportation of firearms and ammunition to new types of stalking and domestic violence offenders.</p><p>Specifically, the bill extends federal firearms-related restrictions to individuals who are convicted of a misdemeanor crime of stalking. The term <em>misdemeanor crime of stalking</em> means a federal, state, tribal, or local offense involving harassment, intimidation, or surveillance that (1) causes emotional distress; or (2) places a person in reasonable fear of harm to themselves, an immediate family member, a current or former cohabitant, an intimate partner, or a pet.</p><p>Additionally, the bill extends federal firearms-related restrictions to individuals who are subject to a domestic violence protection order that restrains them from harassing, stalking, or threatening a current or former dating partner (regardless of when the relationship occurred) or an individual similarly situated to a spouse. Currently, the restrictions only apply if the domestic violence protection order restrains the individual from harassing, stalking, or threatening a co-parent, a current or former spouse, or a current or former cohabitant.</p><p>Finally, the bill extends federal firearms-related restrictions to individuals who commit a misdemeanor crime of domestic violence against the child of a current or recent former dating partner. Currently, the restrictions only apply if the offense is committed against a current or recent former dating partner.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119s2196"
    },
    "title": "Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025</strong></p><p>This bill extends federal restrictions on the receipt, possession, shipment, and transportation of firearms and ammunition to new types of stalking and domestic violence offenders.</p><p>Specifically, the bill extends federal firearms-related restrictions to individuals who are convicted of a misdemeanor crime of stalking. The term <em>misdemeanor crime of stalking</em> means a federal, state, tribal, or local offense involving harassment, intimidation, or surveillance that (1) causes emotional distress; or (2) places a person in reasonable fear of harm to themselves, an immediate family member, a current or former cohabitant, an intimate partner, or a pet.</p><p>Additionally, the bill extends federal firearms-related restrictions to individuals who are subject to a domestic violence protection order that restrains them from harassing, stalking, or threatening a current or former dating partner (regardless of when the relationship occurred) or an individual similarly situated to a spouse. Currently, the restrictions only apply if the domestic violence protection order restrains the individual from harassing, stalking, or threatening a co-parent, a current or former spouse, or a current or former cohabitant.</p><p>Finally, the bill extends federal firearms-related restrictions to individuals who commit a misdemeanor crime of domestic violence against the child of a current or recent former dating partner. Currently, the restrictions only apply if the offense is committed against a current or recent former dating partner.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119s2196"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2196is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Protections for Domestic Violence and Stalking Survivors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to define intimate partner to include someone with whom there is or was a dating relationship, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T03:33:23Z"
    }
  ]
}
```
