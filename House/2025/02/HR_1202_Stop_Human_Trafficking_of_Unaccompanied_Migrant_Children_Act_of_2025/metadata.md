# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1202?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1202
- Title: Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1202
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2026-03-03T15:54:02Z
- Update date including text: 2026-03-03T15:54:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-12 - IntroReferral: Sponsor introductory remarks on measure. (CR H668)
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-12 - IntroReferral: Sponsor introductory remarks on measure. (CR H668)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1202",
    "number": "1202",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000603",
        "district": "8",
        "firstName": "Morgan",
        "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
        "lastName": "Luttrell",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-03T15:54:02Z",
    "updateDateIncludingText": "2026-03-03T15:54:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H668)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:01:05Z",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1202ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1202\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Luttrell (for himself, Ms. Tenney , Mr. Scott Franklin of Florida , Mr. Donalds , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish vetting standards for the placement of unaccompanied alien children with sponsors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025 .\n#### 2. Vetting standards for placement of unaccompanied alien children with sponsors\n##### (a) Vetting of prospective sponsors\n**(1) In general**\nBefore an unaccompanied alien child (as defined in section 462(g) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g) )) may be released from the custody of the Secretary of Health and Human Services to the custody of a sponsor, the sponsor shall undergo and complete, to the satisfaction of the Secretary of Health and Human Services and the head of the department of children and family services of the applicable State (or the equivalent State agency) and in consultation with the Attorney General and the Secretary of Homeland Security, a fingerprint background check and vetting process that includes\u2014\n**(A)**\na public records check;\n**(B)**\na check of the National Sex Offender Registry of the Department of Justice, conducted through the public internet website for such registry;\n**(C)**\na Federal Bureau of Investigation National Criminal History check based on digital fingerprints or digitized fingerprints submitted on paper;\n**(D)**\na Child Abuse and Neglect check, obtained on a State-by-State basis; and\n**(E)**\na check of the criminal history repository of the applicable 1 or more States and a police records check of the applicable localities.\n**(2) Adults household members**\nAs part of the vetting process under paragraph (1), each individual who is 18 years of age or older in the household of a prospective sponsor shall undergo and complete all vetting processes required by paragraph (1), to the satisfaction of the Secretary of Health and Human Services and the head of the department of children and family services of the applicable State (or the equivalent State agency) and in consultation with the Attorney General and the Secretary of Homeland Security, before an unaccompanied alien child may be placed in such household.\n##### (b) Limitation on placement with illegal aliens\nThe Secretary of Health and Human Services may not release an unaccompanied alien child to the custody of a sponsor who is an alien unlawfully present in the United States, unless such alien is a biological parent, legal guardian, or relative of the child.\n##### (c) Monitoring visits\n**(1) Pre-release**\nBefore an unaccompanied alien child may be released from the custody of the Secretary of Health and Human Services, the Secretary shall conduct a home visit to the household in which the child is proposed to be placed, regardless of the sponsor category of the prospective sponsor.\n**(2) Post-release**\nFor each child released from the custody of the Secretary of Health and Human Services after the date of the enactment of this Act, the Secretary shall conduct\u2014\n**(A)**\nduring the 1-year period beginning on the date on which the child is so released, not fewer than 5 unannounced in-person home visits; and\n**(B)**\nduring the subsequent 1-year period, 1 in-person home visit each quarter.\n##### (d) Retroactive vetting\nThe Secretary of Health and Human Services, in collaboration with the head of the department of children and family services of each applicable State (or the equivalent State agency) and in consultation with the Attorney General and the Secretary of Homeland Security, shall immediately conduct the fingerprint background check and vetting process described in subsection (a) for each sponsor with whom a child released from the custody of the Secretary of Health and Human Services has been placed since January 20, 2021, until the sponsor of each such child has been vetted in accordance with this Act.\n##### (e) Monthly reports\n**(1) Children in custody and released to sponsors**\nNot later than 30 days after the date of the enactment of this Act, and every 30 days thereafter, the Secretary of Health and Human Services and the Secretary of Homeland Security shall jointly submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives a report that contains, for the preceding month\u2014\n**(A)**\nthe number of unaccompanied alien children encountered by the Secretary of Homeland Security;\n**(B)**\nthe number of unaccompanied alien children released by the Secretary of Homeland Security into the custody of the Secretary of Health and Human Services;\n**(C)**\nthe number of sponsor background checks completed under subsection (a);\n**(D)**\nthe number of sponsor background checks in progress under such subsection;\n**(E)**\nthe number of pre-release home visits completed;\n**(F)**\nthe number of post-release home visits completed;\n**(G)**\nthe number of unaccompanied alien children released to sponsors, disaggregated by sponsor category;\n**(H)**\ntotal number of unaccompanied alien children in the custody of the Secretary of Health and Human Services, disaggregated by State and Department of Health and Human Services facility; and\n**(I)**\nthe rate at which the Secretary of Health and Human Services rejected sponsorship applications.\n**(2) Missing children**\nNot later than 30 days after the date of the enactment of this Act, and every 30 days thereafter, the Secretary of Health and Human Services and the Secretary of Homeland Security shall jointly submit to Congress a report on all efforts made, during the preceding month, by the Department of Health and Human Services and the Department of Homeland Security to account for all children\u2014\n**(3)**\nwho were released from the custody of the Secretary of Health and Human Services to a sponsor on or after January 20, 2021; and\n**(4)**\nas of the date of the enactment of this Act\u2014\n**(A)**\nwho have been reported missing; or\n**(B)**\nwith respect to whom the Secretary of Health and Human Services has no record since the date of release from custody.",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-01-28",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "286",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025",
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
        "name": "Immigration",
        "updateDate": "2025-03-12T15:13:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hr1202",
          "measure-number": "1202",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2026-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1202v00",
            "update-date": "2026-03-03"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025</strong></p><p>This bill establishes requirements relating to placing unaccompanied alien children with sponsors. (Under federal law, an <em>unaccompanied alien child</em> is a minor with no lawful immigration status and no parent or legal guardian in the United States to provide care and physical custody.)</p><p>Before the Department of Health and Human Services (HHS) may release such a child to a sponsor, the sponsor must complete a fingerprint background check and vetting that includes (1) a public records check, (2) a National Sex Offender Registry check, (3) a Federal Bureau of Investigation National Criminal History Check, (4) a child abuse and neglect check, and (5) state and local criminal history checks. Each adult in the sponsor's household must also undergo such vetting before the placement.</p><p>The bill also requires HHS to visit the home of a proposed sponsor before the placement and to conduct periodic home visits after.</p><p>A child may not be placed with a sponsor who is unlawfully present in the United States unless the sponsor is the child's parent, relative, or legal guardian.</p><p>HHS must retroactively apply these vetting standards to all sponsors for placements made since January 20, 2021.</p>"
        },
        "title": "Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1202.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025</strong></p><p>This bill establishes requirements relating to placing unaccompanied alien children with sponsors. (Under federal law, an <em>unaccompanied alien child</em> is a minor with no lawful immigration status and no parent or legal guardian in the United States to provide care and physical custody.)</p><p>Before the Department of Health and Human Services (HHS) may release such a child to a sponsor, the sponsor must complete a fingerprint background check and vetting that includes (1) a public records check, (2) a National Sex Offender Registry check, (3) a Federal Bureau of Investigation National Criminal History Check, (4) a child abuse and neglect check, and (5) state and local criminal history checks. Each adult in the sponsor's household must also undergo such vetting before the placement.</p><p>The bill also requires HHS to visit the home of a proposed sponsor before the placement and to conduct periodic home visits after.</p><p>A child may not be placed with a sponsor who is unlawfully present in the United States unless the sponsor is the child's parent, relative, or legal guardian.</p><p>HHS must retroactively apply these vetting standards to all sponsors for placements made since January 20, 2021.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr1202"
    },
    "title": "Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025</strong></p><p>This bill establishes requirements relating to placing unaccompanied alien children with sponsors. (Under federal law, an <em>unaccompanied alien child</em> is a minor with no lawful immigration status and no parent or legal guardian in the United States to provide care and physical custody.)</p><p>Before the Department of Health and Human Services (HHS) may release such a child to a sponsor, the sponsor must complete a fingerprint background check and vetting that includes (1) a public records check, (2) a National Sex Offender Registry check, (3) a Federal Bureau of Investigation National Criminal History Check, (4) a child abuse and neglect check, and (5) state and local criminal history checks. Each adult in the sponsor's household must also undergo such vetting before the placement.</p><p>The bill also requires HHS to visit the home of a proposed sponsor before the placement and to conduct periodic home visits after.</p><p>A child may not be placed with a sponsor who is unlawfully present in the United States unless the sponsor is the child's parent, relative, or legal guardian.</p><p>HHS must retroactively apply these vetting standards to all sponsors for placements made since January 20, 2021.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr1202"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1202ih.xml"
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
      "title": "Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Human Trafficking of Unaccompanied Migrant Children Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish vetting standards for the placement of unaccompanied alien children with sponsors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:42Z"
    }
  ]
}
```
