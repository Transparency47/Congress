# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7105?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7105
- Title: Guaranteeing the States Protection Against Invasion Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7105
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-03-16T12:30:06Z
- Update date including text: 2026-03-16T12:30:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7105",
    "number": "7105",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001095",
        "district": "38",
        "firstName": "Wesley",
        "fullName": "Rep. Hunt, Wesley [R-TX-38]",
        "lastName": "Hunt",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Guaranteeing the States Protection Against Invasion Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-16T12:30:06Z",
    "updateDateIncludingText": "2026-03-16T12:30:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:04:30Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7105ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7105\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Hunt introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to provide authority to suspend entry and immigration benefits during a declared invasion at the southern border of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guaranteeing the States Protection Against Invasion Act of 2026 .\n#### 2. Declaration of invasion at southern border\nChapter 2 of title II of the Immigration and Nationality Act ( 8 U.S.C. 1181 et seq. ) is amended by inserting after section 212 the following:\n212A. Declaration of invasion at southern border (a) Authority The President may determine and proclaim that an invasion exists at the southern border of the United States for purposes of article IV, section 4 of the Constitution. (b) Southern border defined In this section, the term southern border means the international land border between the United States and Mexico. (c) Notification Not later than 7 days after issuing or terminating a proclamation under subsection (a), the President shall transmit notice of such action to the Congress. .\n#### 3. Suspension of entry during declared invasion\nSection 212(f) of the Immigration and Nationality Act ( 8 U.S.C. 1182(f) ) is amended\u2014\n**(1)**\nby striking Whenever the President finds and inserting (1) Whenever the President finds ; and\n**(2)**\nby adding at the end the following:\n(2) Notwithstanding any other provision of law, during a period in which the President has proclaimed the existence of an invasion under section 212A, the President shall suspend the entry, including the physical entry, of any alien who unlawfully enters or attempts to enter the United States across the southern border. .\n#### 4. Ineligibility for immigration relief during invasion\nChapter 4 of title II of the Immigration and Nationality Act ( 8 U.S.C. 1151 et seq. ) is amended by inserting after section 208 the following:\n208A. Ineligibility for relief during declared invasion (a) Ineligibility Notwithstanding any other provision of this Act, an alien who unlawfully enters or attempts to enter the United States across the southern border during a period in which an invasion is proclaimed under section 212A shall be ineligible for any relief, protection, or benefit under this Act that would permit the alien to remain in the United States. (b) Covered relief Subsection (a) applies to relief or protection under\u2014 (1) section 208; (2) section 241(b)(3); (3) section 212(d)(5); and (4) any other provision specified by the Secretary of Homeland Security. (c) No jurisdiction No court shall have jurisdiction to review any determination, action, or claim arising under this section, except for a claim that the alien is a national of the United States. .\n#### 5. Public health and security information requirement\n##### (a) Requirement\nSection 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) is amended by adding at the end the following:\n(10) Failure to provide required information during invasion Any alien who, during a period in which an invasion is proclaimed under section 212A, fails prior to entry to provide information sufficient to permit a determination under paragraphs (1), (2), and (3) shall be inadmissible. .\n##### (b) Consequence\nAn alien described in section 212(a)(10) shall be subject to immediate removal, repatriation, or transfer.\n#### 6. Authority to repel and remove\n##### (a) In general\nDuring a period in which an invasion is proclaimed under section 212A, the Secretary of Homeland Security, in coordination with the Secretary of State and the Attorney General, shall take such actions as are necessary to\u2014\n**(1)**\nrepel the invasion;\n**(2)**\ndetain, expel, or remove aliens involved in the invasion; and\n**(3)**\nprevent the further entry of such persons into the United States.\n##### (b) Use of resources\nThe President may direct the use of Federal personnel and assets to carry out subsection (a).\n#### 7. Termination\nThe authorities under sections 212A, 212(f)(2), and 208A of the Immigration and Nationality Act shall cease to apply upon a presidential proclamation that the invasion has ended.",
      "versionDate": "2026-01-15",
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
        "name": "Immigration",
        "updateDate": "2026-03-16T12:30:06Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7105ih.xml"
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
      "title": "Guaranteeing the States Protection Against Invasion Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-14T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guaranteeing the States Protection Against Invasion Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-14T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to provide authority to suspend entry and immigration benefits during a declared invasion at the southern border of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-14T03:48:24Z"
    }
  ]
}
```
