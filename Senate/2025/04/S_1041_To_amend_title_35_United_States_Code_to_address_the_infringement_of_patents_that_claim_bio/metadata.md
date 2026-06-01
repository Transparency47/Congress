# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1041?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1041
- Title: Affordable Prescriptions for Patients Act
- Congress: 119
- Bill type: S
- Bill number: 1041
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-09-03T15:24:06Z
- Update date including text: 2025-09-03T15:24:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported with amendments favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 44.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-03 - Committee: Committee on the Judiciary. Ordered to be reported with amendments favorably.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2025-04-10 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2025-04-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 44.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1041",
    "number": "1041",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Affordable Prescriptions for Patients Act",
    "type": "S",
    "updateDate": "2025-09-03T15:24:06Z",
    "updateDateIncludingText": "2025-09-03T15:24:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 44.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with amendments favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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
        "item": [
          {
            "date": "2025-04-10T20:58:13Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-03T14:15:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-13T18:27:30Z",
            "name": "Referred To"
          }
        ]
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
      "sponsorshipDate": "2025-03-13",
      "state": "CT"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "IA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1041is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1041\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Cornyn (for himself, Mr. Blumenthal , Mr. Grassley , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 35, United States Code, to address the infringement of patents that claim biological products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Affordable Prescriptions for Patients Act .\n#### 2. Patent infringement; Medicare Improvement Fund\n##### (a) In general\nSection 271(e) of title 35, United States Code, is amended\u2014\n**(1)**\nin paragraph (2)(C), in the flush text following clause (ii), by adding at the end the following: With respect to a submission described in clause (ii), the act of infringement shall extend to any patent that claims the biological product, a method of using the biological product, or a method or product used to manufacture the biological product. ; and\n**(2)**\nby adding at the end the following:\n(7) (A) Subject to subparagraphs (C), (D), and (E), if the sponsor of an approved application for a reference product, as defined in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) ) (referred to in this paragraph as the reference product sponsor ), brings an action for infringement under this section against an applicant for approval of a biological product under section 351(k) of such Act that references that reference product (referred to in this paragraph as the subsection (k) applicant ), the reference product sponsor may assert in the action a total of not more than 20 patents of the type described in subparagraph (B), not more than 10 of which shall have issued after the date specified in section 351(l)(7)(A) of such Act. (B) The patents described in this subparagraph are patents that satisfy each of the following requirements: (i) Patents that claim the biological product that is the subject of an application under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) (or a use of that product) or a method or product used in the manufacture of such biological product. (ii) Patents that are included on the list of patents described in paragraph (3)(A) of section 351(l) of the Public Health Service Act ( 42 U.S.C. 262(l) ), including as provided under paragraph (7) of such section 351(l). (iii) Patents that\u2014 (I) have an actual filing date of more than 4 years after the date on which the reference product is approved; or (II) include a claim to a method in a manufacturing process that is not used by the reference product sponsor. (C) The court in which an action described in subparagraph (A) is brought may increase the number of patents limited under that subparagraph\u2014 (i) if the request to increase that number is made without undue delay; and (ii) (I) if the interest of justice so requires; or (II) for good cause shown, which\u2014 (aa) shall be established if the subsection (k) applicant fails to provide information required by section 351(k)(2)(A) of the Public Health Service Act ( 42 U.S.C. 262(k)(2)(A) ) that would enable the reference product sponsor to form a reasonable belief with respect to whether a claim of infringement under this section could reasonably be asserted; and (bb) may be established\u2014 (AA) if there is a material change to the biological product (or process with respect to the biological product) of the subsection (k) applicant that is the subject of the application; (BB) if, with respect to a patent on the supplemental list described in section 351(l)(7)(A) of Public Health Service Act ( 42 U.S.C. 262(l)(7)(A) ), the patent would have issued before the date specified in such section 351(l)(7)(A) but for the failure of the Office to issue the patent or a delay in the issuance of the patent, as described in paragraph (1) of section 154(b) and subject to the limitations under paragraph (2) of such section 154(b); or (CC) for another reason that shows good cause, as determined appropriate by the court. (D) In determining whether good cause has been shown for the purposes of subparagraph (C)(ii)(II), a court may consider whether the reference product sponsor has provided a reasonable description of the identity and relevance of any information beyond the subsection (k) application that the court believes is necessary to enable the court to form a belief with respect to whether a claim of infringement under this section could reasonably be asserted. (E) The limitation imposed under subparagraph (A)\u2014 (i) shall apply only if the subsection (k) applicant completes all actions required under paragraphs (2)(A), (3)(B)(ii), (5), (6)(C)(i), (7), and (8)(A) of section 351(l) of the Public Health Service Act ( 42 U.S.C. 262(l) ); and (ii) shall not apply with respect to any patent that claims, with respect to a biological product, a method for using that product in therapy, diagnosis, or prophylaxis, such as an indication or method of treatment or other condition of use. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply with respect to an application submitted under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) on or after the date of enactment of this Act.",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1041rs.xml",
      "text": "II\nCalendar No. 44\n119th CONGRESS\n1st Session\nS. 1041\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Cornyn (for himself, Mr. Blumenthal , Mr. Grassley , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nApril 10, 2025 Reported by Mr. Grassley , with amendments Omit the parts struck through and insert the parts printed in italic\nA BILL\nTo amend title 35, United States Code, to address the infringement of patents that claim biological products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Affordable Prescriptions for Patients Act .\n#### 2. Patent infringement ; Medicare Improvement Fund\n##### (a) In general\nSection 271(e) of title 35, United States Code, is amended\u2014\n**(1)**\nin paragraph (2) (C) , in the flush text following clause subparagraph (C) (ii), by adding at the end the following: With respect to a submission described in clause subparagraph (C) (ii), the act of infringement shall extend to any patent that claims the biological product, a method of using the biological product, or a method or product used to manufacture the biological product. ; and\n**(2)**\nby adding at the end the following:\n(7) (A) Subject to subparagraphs (C), (D), and (E), if the sponsor of an approved application for a reference product, as defined in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) ) (referred to in this paragraph as the reference product sponsor ), brings an action for infringement under this section against an applicant for approval of a biological product under section 351(k) of such Act that references that reference product (referred to in this paragraph as the subsection (k) applicant ), the reference product sponsor may assert in the action a total of not more than 20 patents of the type described in subparagraph (B), not more than 10 of which shall have issued after the date specified in section 351(l)(7)(A) of such Act. (B) The patents described in this subparagraph are patents that satisfy each of the following requirements: (i) Patents that claim the biological product that is the subject of an application under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) (or a use of that product) or a method or product used in the manufacture of such biological product. (ii) Patents that are included on the list of patents described in paragraph (3)(A) of section 351(l) of the Public Health Service Act ( 42 U.S.C. 262(l) ), including as provided under paragraph (7) of such section 351(l). (iii) Patents that\u2014 (I) have an actual filing date of more than 4 years after the date on which the reference product is approved; or (II) include a claim to a method in a manufacturing process that is not used by the reference product sponsor. (C) The court in which an action described in subparagraph (A) is brought may increase the number of patents limited under that subparagraph\u2014 (i) if the request to increase that number is made without undue delay; and (ii) (I) if the interest of justice so requires; or (II) for good cause shown, which\u2014 (aa) shall be established if the subsection (k) applicant fails to provide information required by section 351(k)(2)(A) of the Public Health Service Act (42. U.S.C. 262(k)(2)(A)) that would enable the reference product sponsor to form a reasonable belief with respect to whether a claim of infringement under this section could reasonably be asserted; and (bb) may be established\u2014 (AA) if there is a material change to the biological product (or process with respect to the biological product) of the subsection (k) applicant that is the subject of the application; (BB) if, with respect to a patent on the supplemental list described in section 351(l)(7) (A) of the Public Health Service Act ( 42 U.S.C. 262(l)(7) (A) ), the patent would have issued before the date specified in such section 351(l)(7)(A) of such Act but for the failure of the Office to issue the patent or a delay in the issuance of the patent, as described in paragraph (1) of section 154(b) and subject to the limitations under paragraph (2) of such section 154(b); or (CC) for another reason that shows good cause, as determined appropriate by the court. (D) In determining whether good cause has been shown for the purposes of subparagraph (C)(ii)(II), a court may consider whether the reference product sponsor has provided a reasonable description of the identity and relevance of any information beyond the subsection (k) application that the court believes is necessary to enable the court to form a belief with respect to whether a claim of infringement under this section could reasonably be asserted. (E) The limitation imposed under subparagraph (A)\u2014 (i) shall apply only if the subsection (k) applicant completes all actions required under paragraphs (2)(A), (3)(B)(ii), (5), (6)(C)(i), (7), and (8)(A) of section 351(l) of the Public Health Service Act ( 42 U.S.C. 262(l) ); and (ii) shall not apply with respect to any patent that claims, with respect to a biological product, a method for using that product in therapy, diagnosis, or prophylaxis, such as an indication or method of treatment or other condition of use. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply with respect to an application submitted under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) on or after the date of enactment of this Act.",
      "versionDate": "2025-04-10",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Competition and antitrust",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Federal Trade Commission (FTC)",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-04-10T13:38:20Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-10T13:38:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-04-04T13:48:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
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
          "measure-id": "id119s1041",
          "measure-number": "1041",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1041v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Affordable Prescriptions for Patients Act</strong></p><p>This bill limits in certain instances the number of patents that the manufacturer of a biologic drug can assert in a lawsuit against a company seeking to sell a biosimilar version of that drug. (A biologic drug is produced through natural processes or isolated from natural sources. A biosimilar version is substantially similar to the original biologic, which is the reference product, and is often marketed as a less expensive alternative.)</p><p>The bill's provisions apply to an existing framework that gives the biosimilar manufacturer an abbreviated path to Food and Drug Administration approval to sell the biosimilar. Specifically, if the biosimilar manufacturer completes certain actions under the framework, such as sharing certain information about its product with the reference product manufacturer, the bill limits the number of certain patents that the reference product manufacturer may assert in a lawsuit, such as patents that were filed more than four years after the reference product received market approval. The limit shall not apply to patents claiming certain methods for using the biologic drug.</p><p>The court in which the infringement lawsuit is filed may increase the limit if justice so requires or if there is good cause for the increase.</p>"
        },
        "title": "Affordable Prescriptions for Patients Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1041.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Affordable Prescriptions for Patients Act</strong></p><p>This bill limits in certain instances the number of patents that the manufacturer of a biologic drug can assert in a lawsuit against a company seeking to sell a biosimilar version of that drug. (A biologic drug is produced through natural processes or isolated from natural sources. A biosimilar version is substantially similar to the original biologic, which is the reference product, and is often marketed as a less expensive alternative.)</p><p>The bill's provisions apply to an existing framework that gives the biosimilar manufacturer an abbreviated path to Food and Drug Administration approval to sell the biosimilar. Specifically, if the biosimilar manufacturer completes certain actions under the framework, such as sharing certain information about its product with the reference product manufacturer, the bill limits the number of certain patents that the reference product manufacturer may assert in a lawsuit, such as patents that were filed more than four years after the reference product received market approval. The limit shall not apply to patents claiming certain methods for using the biologic drug.</p><p>The court in which the infringement lawsuit is filed may increase the limit if justice so requires or if there is good cause for the increase.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s1041"
    },
    "title": "Affordable Prescriptions for Patients Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Affordable Prescriptions for Patients Act</strong></p><p>This bill limits in certain instances the number of patents that the manufacturer of a biologic drug can assert in a lawsuit against a company seeking to sell a biosimilar version of that drug. (A biologic drug is produced through natural processes or isolated from natural sources. A biosimilar version is substantially similar to the original biologic, which is the reference product, and is often marketed as a less expensive alternative.)</p><p>The bill's provisions apply to an existing framework that gives the biosimilar manufacturer an abbreviated path to Food and Drug Administration approval to sell the biosimilar. Specifically, if the biosimilar manufacturer completes certain actions under the framework, such as sharing certain information about its product with the reference product manufacturer, the bill limits the number of certain patents that the reference product manufacturer may assert in a lawsuit, such as patents that were filed more than four years after the reference product received market approval. The limit shall not apply to patents claiming certain methods for using the biologic drug.</p><p>The court in which the infringement lawsuit is filed may increase the limit if justice so requires or if there is good cause for the increase.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s1041"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1041is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1041rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Affordable Prescriptions for Patients Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "title": "Affordable Prescriptions for Patients Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Affordable Prescriptions for Patients Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T22:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 35, United States Code, to address the infringement of patents that claim biological products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T22:18:15Z"
    }
  ]
}
```
