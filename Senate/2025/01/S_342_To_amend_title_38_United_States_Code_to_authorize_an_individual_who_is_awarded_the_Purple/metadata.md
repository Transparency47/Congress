# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/342?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/342
- Title: Purple Heart Veterans Education Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 342
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2026-04-01T18:50:21Z
- Update date including text: 2026-04-01T18:50:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/342",
    "number": "342",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001111",
        "district": "",
        "firstName": "Patty",
        "fullName": "Sen. Murray, Patty [D-WA]",
        "lastName": "Murray",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Purple Heart Veterans Education Act of 2025",
    "type": "S",
    "updateDate": "2026-04-01T18:50:21Z",
    "updateDateIncludingText": "2026-04-01T18:50:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
            "date": "2026-03-18T20:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-01-30T21:32:16Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "NC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "FL"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-30",
      "state": "ME"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "AR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "NV"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "MT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "OR"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "TX"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "AZ"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "ND"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CO"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "GA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s342is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 342\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mrs. Murray (for herself, Mr. Tillis , Mr. Scott of Florida , Mr. King , Mr. Boozman , Ms. Rosen , Mr. Daines , Mr. Wyden , Mr. Cornyn , Mr. Kelly , Mr. Cramer , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to authorize an individual who is awarded the Purple Heart for service in the Armed Forces to transfer unused Post-9/11 Educational Assistance to a family member, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Purple Heart Veterans Education Act of 2025 .\n#### 2. Authority for individuals awarded Purple Heart to transfer unused Post-9/11 Educational Assistance to a family member\n##### (a) In general\nSubchapter II of chapter 33 of title 38, United States Code, is amended by inserting after section 3319 the following new section:\n3319A. Authority for recipients of Purple Heart to transfer unused Post-9/11 Educational Assistance to a family member (a) In general The Secretary shall permit an individual described in subsection (b) who is entitled to educational assistance under this chapter to elect to transfer to one or more of the dependents specified in subsection (c) a portion of such individual's entitlement to such assistance, subject to the limitation under subsection (d). (b) Eligible individuals An individual referred to in subsection (a) is any veteran who is awarded, after being discharged or released from service in the active military, naval, air, or space service, the Purple Heart for service in the Armed Forces occurring on or after September 11, 2001. (c) Eligible dependents (1) Transfer An individual approved to transfer an entitlement to educational assistance under this section may transfer the individual's entitlement to an eligible dependent or a combination of eligible dependents. (2) Definition of eligible dependent For purposes of this subsection, the term eligible dependent has the meaning given the term dependent under subparagraphs (A), (D), and (I) of section 1072(2) of title 10. (d) Limitation on months of transfer The total number of months of entitlement transferred by an individual under this section may not exceed 36 months. (e) Designation of transferee An individual transferring an entitlement to educational assistance under this section shall\u2014 (1) designate the dependent or dependents to whom such entitlement is being transferred; and (2) designate the number of months of such entitlement to be transferred to each such dependent. (f) Revocation and modification (1) Modification or revocation (A) In general An individual transferring entitlement under this section may modify or revoke at any time the transfer of any unused portion of the entitlement so transferred. (B) Notice The modification or revocation of the transfer of entitlement under this paragraph shall be made by the submittal of written notice of the action to the Secretary. (2) Prohibition on treatment of transferred entitlement as marital property Entitlement transferred under this section may not be treated as marital property, or the asset of a marital estate, subject to division in a divorce or other civil proceeding. (g) Commencement of use A dependent to whom entitlement to educational assistance is transferred under this section may not commence the use of the transferred entitlement, in the case of entitlement transferred to a child, until either\u2014 (1) the completion by the child of the requirements of a secondary school diploma (or equivalency certificate); or (2) the attainment by the child of 18 years of age. (h) Additional administrative matters (1) Use The use of any entitlement to educational assistance transferred under this section shall be charged against the entitlement of the individual making the transfer at the rate of one month for each month of transferred entitlement that is used. (2) Nature of transferred entitlement Except as provided under subsection (e)(2) and subject to paragraphs (5) and (6), the recipient of entitlement transferred under this section is entitled to educational assistance under this chapter in the same manner as the individual from whom the entitlement was transferred. (3) Rate of payment The monthly rate of educational assistance payable to a dependent to whom entitlement referred to in paragraph (2) is transferred under this section shall be payable at the same rate as such entitlement would otherwise be payable under this chapter to the individual making the transfer. (4) Death of transferor (A) In general The death of an individual transferring an entitlement under this section shall not affect the use of the entitlement by the dependent to whom the entitlement is transferred. (B) Death prior to transfer to designated transferees (i) In the case of an eligible individual whom the Secretary, in consultation with the Secretary of Defense, has approved to transfer the individual's entitlement under this section who, at the time of death, is entitled to educational assistance under this chapter and has designated a transferee or transferees under subsection (e) but has not transferred all of such entitlement to such transferee or transferees, the Secretary shall transfer the entitlement of the individual under this section by evenly distributing the amount of such entitlement between all such transferees who would not be precluded from using some or all of the transferred benefits due to the expiration of time limitations found in paragraph (5) of this subsection or section 3321 of this title, notwithstanding the limitations under subsection (f). (ii) If a transferee cannot use all of the transferred benefits under clause (i) because of expiration of a time limitation, the unused benefits will be distributed among the other designated transferees who would not be precluded from using some or all of the transferred benefits due to expiration of time limitations found in paragraph (5) of this subsection or section 3321 of this title, unless or until there are no transferees who would not be precluded from using the transferred benefits because of expiration of a time limitation. (5) Limitation on age of use by child transferees (A) In general A child to whom entitlement is transferred under this section may use the benefits transferred without regard to the 15-year delimiting date specified in section 3321 of this title, but may not, except as provided in subparagraph (B) or (C), use any benefits so transferred after attaining the age of 26 years. (B) Primary caregivers of seriously injured members of the armed forces and veterans (i) In general Subject to clause (ii), in the case of a child who, before attaining the age of 26 years, is prevented from pursuing a chosen program of education by reason of acting as the primary provider of personal care services for a veteran or member of the Armed Forces under section 1720G(a) of this title, the child may use the benefits beginning on the date specified in clause (iii) for a period whose length is specified in clause (iv). (ii) Inapplicability for revocation Clause (i) shall not apply with respect to the period of an individual as a primary provider of personal care services if the period concludes with the revocation of the individual's designation as such a primary provider under section 1720G(a)(7)(D) of this title. (iii) Date for commencement of use The date specified in this clause for the beginning of the use of benefits by a child under clause (i) is the later of\u2014 (I) the date on which the child ceases acting as the primary provider of personal care services for the veteran or member concerned as described in clause (i); (II) the date on which it is reasonably feasible, as determined under regulations prescribed by the Secretary, for the child to initiate or resume the use of benefits; or (III) the date on which the child attains the age of 26 years. (iv) Length of use The length of the period specified in this clause for the use of benefits by a child under clause (i) is the length equal to the length of the period that\u2014 (I) begins on the date on which the child begins acting as the primary provider of personal care services for the veteran or member concerned as described in clause (i); and (II) ends on the later of\u2014 (aa) the date on which the child ceases acting as the primary provider of personal care services for the veteran or member as described in clause (i); or (bb) the date on which it is reasonably feasible, as so determined, for the child to initiate or resume the use of benefits. (C) Emergency situations In any case in which the Secretary determines that an individual to whom entitlement is transferred under this section has been prevented from pursuing the individual's chosen program of education before the individual attains the age of 26 years because the educational institution or training establishment closed (temporarily or permanently) under an established policy based on an Executive order of the President or due to an emergency situation, the Secretary shall extend the period during which the individual may use such entitlement for a period equal to the number of months that the individual was so prevented from pursuing the program of education, as determined by the Secretary. (6) Scope of use by transferees The purposes for which a dependent to whom entitlement is transferred under this section may use such entitlement shall include the pursuit and completion of the requirements of a secondary school diploma (or equivalency certificate). (7) Additional administrative provisions The administrative provisions of this chapter shall apply to the use of entitlement transferred under this section, except that the dependent to whom the entitlement is transferred shall be treated as the eligible individual for purposes of such provisions. (i) Overpayment In the event of an overpayment of educational assistance with respect to a dependent to whom entitlement is transferred under this section, the dependent and the individual making the transfer shall be jointly and severally liable to the United States for the amount of the overpayment for purposes of section 3685 of this title. (j) Regulations (1) The Secretary shall, in consultation with the Secretary of Defense, prescribe regulations for purposes of this section. (2) Such regulations shall specify\u2014 (A) the manner of authorizing the transfer of entitlements under this section; (B) the eligibility criteria in accordance with subsection (b); and (C) the manner and effect of an election to modify or revoke a transfer of entitlement under subsection (f)(1). (k) Transfer by dependent In the case of an individual who transfers entitlement to educational assistance under this section who dies before the dependent to whom entitlement to educational assistance is so transferred has used all of such entitlement, such dependent may transfer such entitlement to another eligible dependent in accordance with the provisions of this section. (l) Coordination The Secretary of Veterans Affairs and the Secretary of Defense shall coordinate with each other to facilitate the transfer of entitlement under this section. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 3319 the following new item:\n3319A. Authority for recipients of Purple Heart to transfer unused Post-9/11 Educational Assistance to a family member. .",
      "versionDate": "2025-01-30",
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
        "actionDate": "2025-03-04",
        "text": "Referred to the Subcommittee on Economic Opportunity."
      },
      "number": "790",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend title 38, United States Code, to authorize an individual who is awarded the Purple Heart for service in the Armed Forces to transfer unused Post-9/11 Educational Assistance to a family member, and for other purposes.",
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
            "name": "Family relationships",
            "updateDate": "2025-03-27T15:46:53Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-27T15:46:53Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-03-27T15:46:53Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-03-27T15:46:53Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-03-27T15:46:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-18T17:44:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119s342",
          "measure-number": "342",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-03-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s342v00",
            "update-date": "2025-03-20"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Purple Heart Veterans Education Act of 2025</strong></p><p>This bill authorizes certain Purple Heart recipients to elect to transfer to one or more eligible dependents (e.g., a spouse or child) unused portions of such recipients\u2019 entitlement to Post-9/11 GI Bill educational assistance. This authority specifically applies to veterans who are awarded the Purple Heart for service in the Armed Forces occurring on or after September 11, 2001, and who have been discharged or released from active service.</p><p>Under the bill, the total number of months of entitlement transferred by a Purple Heart recipient may not exceed 36 months. Additionally, the Purple Heart recipient may modify or revoke any unused portion of the transferred entitlement by submitting written notice.</p><p>A transferred entitlement may not be treated as marital property or marital assets in divorce or other civil proceedings.</p><p>The death of the Purple Heart recipient must not affect the use of the entitlement by the individual who receives the transferred entitlement.</p><p>In the event of an overpayment of educational assistance, the Purple Heart recipient and the transferee of the entitlement must be held jointly and severally liable for the amount.</p><p>The bill requires the VA and DOD to coordinate to facilitate the transfer of entitlements under the bill.</p>"
        },
        "title": "Purple Heart Veterans Education Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s342.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Purple Heart Veterans Education Act of 2025</strong></p><p>This bill authorizes certain Purple Heart recipients to elect to transfer to one or more eligible dependents (e.g., a spouse or child) unused portions of such recipients\u2019 entitlement to Post-9/11 GI Bill educational assistance. This authority specifically applies to veterans who are awarded the Purple Heart for service in the Armed Forces occurring on or after September 11, 2001, and who have been discharged or released from active service.</p><p>Under the bill, the total number of months of entitlement transferred by a Purple Heart recipient may not exceed 36 months. Additionally, the Purple Heart recipient may modify or revoke any unused portion of the transferred entitlement by submitting written notice.</p><p>A transferred entitlement may not be treated as marital property or marital assets in divorce or other civil proceedings.</p><p>The death of the Purple Heart recipient must not affect the use of the entitlement by the individual who receives the transferred entitlement.</p><p>In the event of an overpayment of educational assistance, the Purple Heart recipient and the transferee of the entitlement must be held jointly and severally liable for the amount.</p><p>The bill requires the VA and DOD to coordinate to facilitate the transfer of entitlements under the bill.</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119s342"
    },
    "title": "Purple Heart Veterans Education Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Purple Heart Veterans Education Act of 2025</strong></p><p>This bill authorizes certain Purple Heart recipients to elect to transfer to one or more eligible dependents (e.g., a spouse or child) unused portions of such recipients\u2019 entitlement to Post-9/11 GI Bill educational assistance. This authority specifically applies to veterans who are awarded the Purple Heart for service in the Armed Forces occurring on or after September 11, 2001, and who have been discharged or released from active service.</p><p>Under the bill, the total number of months of entitlement transferred by a Purple Heart recipient may not exceed 36 months. Additionally, the Purple Heart recipient may modify or revoke any unused portion of the transferred entitlement by submitting written notice.</p><p>A transferred entitlement may not be treated as marital property or marital assets in divorce or other civil proceedings.</p><p>The death of the Purple Heart recipient must not affect the use of the entitlement by the individual who receives the transferred entitlement.</p><p>In the event of an overpayment of educational assistance, the Purple Heart recipient and the transferee of the entitlement must be held jointly and severally liable for the amount.</p><p>The bill requires the VA and DOD to coordinate to facilitate the transfer of entitlements under the bill.</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119s342"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s342is.xml"
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
      "title": "Purple Heart Veterans Education Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Purple Heart Veterans Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to authorize an individual who is awarded the Purple Heart for service in the Armed Forces to transfer unused Post-9/11 Educational Assistance to a family member, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:04:02Z"
    }
  ]
}
```
