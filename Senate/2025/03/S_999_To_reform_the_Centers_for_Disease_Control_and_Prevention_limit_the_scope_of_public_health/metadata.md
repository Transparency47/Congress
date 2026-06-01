# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/999?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/999
- Title: Public Health Improvement Act
- Congress: 119
- Bill type: S
- Bill number: 999
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-01-06T22:03:19Z
- Update date including text: 2026-01-06T22:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/999",
    "number": "999",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Public Health Improvement Act",
    "type": "S",
    "updateDate": "2026-01-06T22:03:19Z",
    "updateDateIncludingText": "2026-01-06T22:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T20:17:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s999is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 999\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Schmitt (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reform the Centers for Disease Control and Prevention, limit the scope of public health authorities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Health Improvement Act .\n#### 2. Terms of CDC and NIH directors\n##### (a) Term of CDC director\nSection 305(a) of the Public Health Service Act ( 42 U.S.C. 242c(a) ) is amended by adding at the end the following: No individual may serve as Director for a total period of more than 12 years. .\n##### (b) Term of NIH director\nSection 402(a) of the Public Health Service Act ( 42 U.S.C. 282(a) ) is amended by adding at the end the following: No individual may serve as Director of NIH for a total period of more than 12 years. .\n#### 3. Limiting the CDC strategic plan\nSection 305(c)(2)(A) of the Public Health Service Act ( 42 U.S.C. 242c(c)(2)(A) ) is amended\u2014\n**(1)**\nin clause (i), by striking and noncommunicable diseases or conditions, and addressing injuries, and occupational and environmental hazards and inserting diseases ;\n**(2)**\nin clause (ii), by striking or conditions ;\n**(3)**\nin clause (iii), by adding and at the end;\n**(4)**\nin clause (iv), by striking ; and and inserting a semicolon; and\n**(5)**\nby striking clause (v).\n#### 4. Advisory committee to the CDC Director\nSection 305A(c) of the Public Health Service Act ( 42 U.S.C. 242c\u20131(c) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking by the Secretary under and inserting as described in ; and\n**(2)**\nin paragraph (3), by striking subparagraphs (A) and (B) and inserting the following:\n(A) Three members shall be appointed by the Secretary of Health and Human Services\u2014 (i) 1 of whom shall be appointed to represent the Department of Health and Human Services; and (ii) 1 of whom shall be a public health official. (B) Two members shall be appointed by the majority leader of the Senate. (C) Two members shall be appointed by the minority leader of the Senate. (D) Two members shall be appointed by the Speaker of the House of Representatives. (E) Two members shall be appointed by the minority leader of the House of Representatives. (F) Four members shall be appointed by the Comptroller General of the United States. .\n#### 5. Limiting the scope of regulations of the Department of Health and Human Services to control communicable diseases\nSection 361(a) of the Public Health Service Act ( 42 U.S.C. 264(a) ) is amended to read as follows:\n(a) To prevent the introduction, transmission, or spread of communicable diseases from foreign countries into the States or possessions, or from one State or possession into any other State or possession, the Secretary may make and enforce regulations for the inspection, fumigation, disinfection, sanitation, pest extermination, or destruction of animals or articles found to be so infected or contaminated as to be sources of dangerous infection to human beings. .\n#### 6. Congressional approval for public health emergencies\nSection 319(a) of the Public Health Service Act ( 42 U.S.C. 247d(a) ) is amended by striking the third and fourth sentences and inserting the following: Determinations that terminate under the preceding sentence may be renewed by a majority vote in both chambers of Congress, and such a renewal period terminates upon the Secretary declaring that the emergency no longer exists or the expiration of the 90-day period beginning on the date on which both chambers of Congress have voted in favor of such renewal, whichever occurs first. Not later than 48 hours after making a determination under this subsection of a public health emergency, the Secretary shall submit to the Congress written notification of the determination. .\n#### 7. Transfer of offices to NIH\n##### (a) In general\nEffective on the date that is 2 years after the date of enactment of this Act, notwithstanding any other provision of law, the authorities, functions, personnel, and assets of the offices described in subsection (b) shall be transferred from the Centers for Disease Control and Prevention to the National Institutes of Health.\n##### (b) Offices described\nThe offices described in this subsection are the following:\n**(1)**\nThe National Center on Birth Defects and Developmental Disabilities.\n**(2)**\nThe National Center for Chronic Disease Prevention and Health Promotion.\n**(3)**\nThe National Center for Environmental Health.\n**(4)**\nThe Agency for Toxic Substances and Disease Registry.\n**(5)**\nThe National Center for Health Statistics.\n**(6)**\nThe National Center for HIV, Viral Hepatitis, STD, and Tuberculosis Prevention.\n**(7)**\nThe National Center for Injury Prevention and Control.\n**(8)**\nThe National Institute for Occupational Safety and Health.\n#### 8. Regulations\nNot later than 90 days after the date of enactment of this Act, the Secretary of Health and Human Services shall issue such new or revised regulations as are necessary to carry out this Act (including the amendments made by this Act).\n#### 9. Preemption\nThe provisions of this Act (including the amendments made by this Act) shall supersede any provision of Federal, State, Tribal, territorial, or local law, declaration, guidance, or directive to the extent that such law, declaration, guidance, or directive is inconsistent with this Act (including such amendments).",
      "versionDate": "2025-03-12",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-03-31T16:02:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119s999",
          "measure-number": "999",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2026-01-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s999v00",
            "update-date": "2026-01-06"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Public Health Improvement Act</strong></p><p>This bill narrows the authority of the Department of Health and Human Services (HHS) with respect to the control of communicable diseases and renewals of public health emergencies. It also limits the priorities of the Centers for Disease Control and Prevention (CDC) to solely communicable diseases.\u00a0</p><p>Specifically, the bill removes HHS' discretion to take measures it deems necessary to prevent the spread of communicable diseases. It also narrows the objectives and priorities of the\u00a0CDC\u00a0by removing noncommunicable diseases, injuries, occupational and environmental hazards, and discretionary priorities from its strategic plan.</p><p>Also, the bill removes the authority of HHS to renew a declaration of a public health emergency and instead requires Congress to issue a renewal. </p><p>The bill also limits the terms of the directors of the CDC and the National Institutes of Health (NIH) to 12 years and requires members of the Advisory Committee to the Director of the CDC to be appointed by members of Congress and other officials (currently appointed by the director).\u00a0Additionally, the bill transfers eight offices from the CDC to the NIH (e.g., the National Institute for Occupational Safety and Health).\u00a0</p>"
        },
        "title": "Public Health Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s999.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Public Health Improvement Act</strong></p><p>This bill narrows the authority of the Department of Health and Human Services (HHS) with respect to the control of communicable diseases and renewals of public health emergencies. It also limits the priorities of the Centers for Disease Control and Prevention (CDC) to solely communicable diseases.\u00a0</p><p>Specifically, the bill removes HHS' discretion to take measures it deems necessary to prevent the spread of communicable diseases. It also narrows the objectives and priorities of the\u00a0CDC\u00a0by removing noncommunicable diseases, injuries, occupational and environmental hazards, and discretionary priorities from its strategic plan.</p><p>Also, the bill removes the authority of HHS to renew a declaration of a public health emergency and instead requires Congress to issue a renewal. </p><p>The bill also limits the terms of the directors of the CDC and the National Institutes of Health (NIH) to 12 years and requires members of the Advisory Committee to the Director of the CDC to be appointed by members of Congress and other officials (currently appointed by the director).\u00a0Additionally, the bill transfers eight offices from the CDC to the NIH (e.g., the National Institute for Occupational Safety and Health).\u00a0</p>",
      "updateDate": "2026-01-06",
      "versionCode": "id119s999"
    },
    "title": "Public Health Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Public Health Improvement Act</strong></p><p>This bill narrows the authority of the Department of Health and Human Services (HHS) with respect to the control of communicable diseases and renewals of public health emergencies. It also limits the priorities of the Centers for Disease Control and Prevention (CDC) to solely communicable diseases.\u00a0</p><p>Specifically, the bill removes HHS' discretion to take measures it deems necessary to prevent the spread of communicable diseases. It also narrows the objectives and priorities of the\u00a0CDC\u00a0by removing noncommunicable diseases, injuries, occupational and environmental hazards, and discretionary priorities from its strategic plan.</p><p>Also, the bill removes the authority of HHS to renew a declaration of a public health emergency and instead requires Congress to issue a renewal. </p><p>The bill also limits the terms of the directors of the CDC and the National Institutes of Health (NIH) to 12 years and requires members of the Advisory Committee to the Director of the CDC to be appointed by members of Congress and other officials (currently appointed by the director).\u00a0Additionally, the bill transfers eight offices from the CDC to the NIH (e.g., the National Institute for Occupational Safety and Health).\u00a0</p>",
      "updateDate": "2026-01-06",
      "versionCode": "id119s999"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s999is.xml"
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
      "title": "Public Health Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public Health Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reform the Centers for Disease Control and Prevention, limit the scope of public health authorities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:33:43Z"
    }
  ]
}
```
