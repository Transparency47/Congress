# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3373?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3373
- Title: GHOST Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3373
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2025-11-13T09:05:37Z
- Update date including text: 2025-11-13T09:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3373",
    "number": "3373",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "GHOST Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-13T09:05:37Z",
    "updateDateIncludingText": "2025-11-13T09:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
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
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:07:35Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "DC"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "GA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "DE"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "PA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "OR"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "WA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NJ"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "OR"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "MI"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MD"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NC"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "MO"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "VA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "VT"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "NM"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "TX"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3373ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3373\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Ms. Tokuda (for herself, Ms. Norton , Mr. Johnson of Georgia , Mr. Casar , Ms. McBride , Mr. Krishnamoorthi , Ms. Kelly of Illinois , Ms. Dean of Pennsylvania , Mr. Garcia of California , Ms. Ansari , Mr. Tran , Mr. Levin , Ms. Bonamici , Ms. Randall , Ms. Vel\u00e1zquez , Mr. Davis of Illinois , Ms. Escobar , Mr. Goldman of New York , Mrs. McIver , Ms. Salinas , Mr. Min , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo create a system to report the movement of firearm parts across State lines, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gun Hardware Oversight and Shipment Tracking Act of 2025 or the GHOST Act of 2025 .\n#### 2. Federal Interstate Firearm Parts Reporting System\n##### (a) In general\nChapter 44 of title 18, United States Code, is amended by adding at the end the following:\n935. Federal Interstate Firearm Parts Reporting System (a) Establishment The Attorney General shall establish and operate a program under this section, to be known as the Federal Interstate Firearm Parts Reporting System , to assist law enforcement officers in monitoring the shipment or transportation of covered firearm components in interstate or foreign commerce. (b) Registration requirement (1) In general Within 5 business days before an entity ships or transports in interstate or foreign commerce a covered firearm component, the entity shall register the shipment or transportation of the covered firearm component by submitting to the Attorney General, in such form and manner determined by the Attorney General, the following information: (A) The name, physical mailing address, phone number or electronic mail address, and the eligible identification number of the entity. (B) The name, physical mailing address, phone number or electronic mail address, and the eligible identification number of the intended recipient of the covered firearm component. (C) The method by which the entity is shipping or transporting the covered firearm component, such as by mail, personal delivery, or delivery by courier, and the name of the shipper or transporter. (D) A list or manifest of the items in, or a bill of lading with respect to, the package or cargo containing the covered firearm component, prepared by the entity for the shipment or transportation. (2) Requirement for delivery (A) Postal delivery to require registered or certified mail An entity using the mails to ship or transport a covered firearm component in interstate or foreign commerce shall use registered or certified mail, return receipt requested, or an equivalent service determined by the Attorney General in consultation with the United States Postal Service. (B) Other forms of delivery to require signature of recipient An entity using a means other than the mails to ship or transport a covered firearm component in interstate or foreign commerce a covered firearm component by delivery shall obtain, cause to obtain, or use a service that requires, the signature of the recipient on delivery and notification to the entity of the signature. (3) Confirmation of delivery Within 5 business days after submitting to the Attorney General the information described in paragraph (1), an entity that ships or transports in interstate or foreign commerce a covered firearm component shall submit to the Attorney General the date that the entity began the shipment or transportation and\u2014 (A) (i) any documentation received by the entity with respect to the delivery; and (ii) the date that the recipient received the covered firearm component according to the documentation; or (B) a certification that the entity has not received the documentation, in which case the entity shall comply with subparagraph (A) at the earliest possible opportunity and submit an additional such certification every 5 business days thereafter until\u2014 (i) the entity is able to, and does, comply with subparagraph (A); or (ii) the Attorney General informs the entity that additional certifications are not required. (4) Safe harbor provisions (A) Retroactive registration after shipment or transportation Subject to subparagraph (C), an entity that ships or transports in interstate or foreign commerce a covered firearm component without complying with paragraph (1) may retroactively register the shipment or transportation of the covered firearm component by submitting to the Attorney General the information required by paragraph (1) not later than 5 business days after the completion of delivery. (B) Putative registration by recipient The recipient of a covered firearm component shipped or transported in interstate or foreign commerce may file a putative registration of the shipment or transportation of the covered firearm component by submitting to the Attorney General, not later than 5 business days after receiving the covered firearm component\u2014 (i) such information required under paragraph (1) available to the recipient, with a certification that the information is accurate and complete to the best of the ability of the recipient; or (ii) a written assurance provided to the recipient by the entity that shipped or transported the covered firearm component that contains the information required under paragraph (1). (C) Discretion of Attorney General to prohibit retroactive registration The Attorney General may prohibit an entity from retroactively registering the shipment or transportation of a covered firearm component under subparagraph (A) if the Attorney General\u2014 (i) determines that the entity routinely fails to comply with paragraph (1) and relies on subparagraph (A) for the registration of a shipment or transportation of a covered firearm component; and (ii) provides notice to the entity of the determination described in clause (i). (c) Database of registrations (1) In general The Attorney General shall compile and maintain a database containing the information gathered under this section. (2) Access to database The Attorney General may disclose information in the database to any of the following: (A) A Federal, State, local, Tribal, or foreign law enforcement agency. (B) A Federal, State, or local prosecutor. (C) A Federal agency. (D) An individual with express authorization from an entity described in any of subparagraphs (A) through (C). (3) Exemption from Freedom of Information Act Except as provided under this section, the information gathered by the Attorney General under this section may not be publicly disclosed and shall be exempt from disclosure under section 552(b)(3) of title 5. (d) Unregistered shipments or transportations of covered firearm components (1) Components subject to seizure The Attorney General, and any government entity designated by the Attorney General, may seize a covered firearm component that was, or is being, shipped or transported in interstate or foreign commerce without registration under subsection (b). (2) Exigent circumstances A law enforcement officer under the authority of a State, local, or Tribal law enforcement agency may seize a covered firearm component described in paragraph (1) if the officer certifies to the Attorney General that exigent circumstances, with a reasonable risk of injury or death, existed at the time of seizure that prevented seizure of the covered firearm component after the Attorney General could have designated the officer or agency under paragraph (1). (3) Administrative proceedings for destruction The Attorney General may use administrative proceedings to provide for the destruction of a covered firearm component seized under paragraph (1) if no person raises an objection to the Attorney General with respect to the destruction. (4) Judicial review If a person raises an objection to destruction of a covered firearm component under paragraph (2), the Attorney General may petition the United States district court for the district in which the Attorney General seized the covered firearm component for an order authorizing the destruction, which shall be granted if the court determines that\u2014 (A) the Attorney General did not receive, with respect to the covered firearm component, a registration under subsection (b)(1), a retroactive registration under subsection (b)(4)(A), or a putative registration under subsection (b)(4)(B); and (B) if the recipient of the covered firearm component had a reasonable opportunity to file a putative registration under subsection (b)(4)(B) with respect to the covered firearm component, the recipient did not file the putative registration. (e) Unlawful acts It shall be unlawful for any person to knowingly ship or transport in interstate or foreign commerce a covered firearm component without registration under subsection (b), with intent to evade the registration requirements of this section. (f) Authority To prescribe regulations The Attorney General may prescribe regulations to carry out this section, which may include regulations describing the administrative proceedings referred to in subsection (d)(3). (g) Definitions In this section and section 924(q): (1) Covered firearm component The term covered firearm component means the barrel, slide, or bolt carrier of a firearm. (2) Eligible identification number The term eligible identification number means, with respect to an entity\u2014 (A) the identifying number assigned to the entity under section 6109 of the Internal Revenue Code of 1986; (B) the last 4 digits of the social security number of the entity; or (C) an identification number approved by the Attorney General that uniquely identifies the entity. .\n##### (b) Penalties\nSection 924 of such title is amended by adding at the end the following:\n(q) Any person who knowingly violates section 935(e)\u2014 (1) shall be fined under this title, imprisoned not more than 1 year, or both; and (2) if the offense includes the shipment or transportation of not less than 50 covered firearm components as part of a single act, commission, conspiracy, or enterprise, shall be fined under this title, imprisoned not more than 10 years, or both. .\n##### (c) Clerical amendment\nThe table of contents for such chapter is amended by adding at the end the following:\n935. Federal Interstate Firearm Parts Reporting System. .\n##### (d) Effective date\nThe amendments made by this Act shall take effect on the date that is 120 days after the date of the enactment of this Act.",
      "versionDate": "2025-05-13",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-28T12:45:22Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3373ih.xml"
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
      "title": "GHOST Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GHOST Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gun Hardware Oversight and Shipment Tracking Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To create a system to report the movement of firearm parts across State lines, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:38Z"
    }
  ]
}
```
