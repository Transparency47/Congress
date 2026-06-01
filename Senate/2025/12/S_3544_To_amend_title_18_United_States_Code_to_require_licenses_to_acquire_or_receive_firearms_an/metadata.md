# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3544?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3544
- Title: Federal Firearm Licensing Act
- Congress: 119
- Bill type: S
- Bill number: 3544
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-20T15:10:22Z
- Update date including text: 2026-01-20T15:10:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3544",
    "number": "3544",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Federal Firearm Licensing Act",
    "type": "S",
    "updateDate": "2026-01-20T15:10:22Z",
    "updateDateIncludingText": "2026-01-20T15:10:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T21:44:57Z",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "HI"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3544is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3544\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Booker (for himself, Mr. Kim , Mr. Schatz , Ms. Warren , Mr. Blumenthal , Mr. Schiff , Mr. Padilla , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to require licenses to acquire or receive firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Firearm Licensing Act .\n#### 2. License for the purchase and possession of firearms\n##### (a) In general\nChapter 44 of title 18, United States Code, is amended by adding at the end the following:\n935. License for the acquisition, receipt, and possession of firearms (a) In general Except as provided in subsection (d), it shall be unlawful for any individual to purchase, receive, or possess a firearm unless the individual has a valid Federal firearm purchasing license. (b) Establishment of Federal license to purchase, receive, or possess firearms (1) In general The Attorney General shall establish a Federal system for issuing a Federal firearm purchasing license to eligible individuals for firearms transferred to such individual or possessed by such individual. (2) Requirements The system established under paragraph (1) shall require that\u2014 (A) an individual shall be eligible to receive such a license if the individual\u2014 (i) has completed training in firearms safety, including\u2014 (I) a written test, to demonstrate knowledge of applicable firearms laws; and (II) hands-on testing, including firing testing, to demonstrate safe use and sufficient accuracy of a firearm; and (ii) as part of the process for applying for such a license\u2014 (I) has submitted to a background investigation and criminal history check of the individual; (II) has submitted proof of identity; (III) has submitted the fingerprints of the individual; and (IV) has submitted identifying information on the firearm that the person intends to obtain, including the make, model, and serial number, and the identity of the firearm seller or transferor; (B) a license issued under the system is available at a designated local office, which shall be located in both urban and rural areas; (C) the Attorney General shall issue or deny a license under this section not later than 30 days after the date on which the application for such license is received; (D) each license issued under this section shall be valid for the purchase of a single firearm, which shall be purchased not later than 30 days after the date on which the license is issued; (E) a license issued under the system shall expire on the date that is 5 years after the date on which the license was issued; and (F) the Attorney General shall provide notice of an application for a license under this section to the relevant State and local officials. (3) Background investigation (A) In general Before issuing a license under this section, the Attorney General shall\u2014 (i) conduct a background investigation on the applicant; and (ii) deny any license if receipt or transfer of a firearm would violate subsection (d), (g), or (n) of section 922 or any provision of State law. (B) Poses a danger of bodily injury (i) Information from State and local officials After receiving the notice described in paragraph (2)(F), relevant State and local officials may submit to the Attorney General information demonstrating that the individual poses a significant danger of bodily injury to self or others by possessing, purchasing, or receiving a firearm. (ii) Denial (I) In general The Attorney General may deny a license under this section if the Attorney General determines that the applicant poses a significant danger of bodily injury to self or others by possessing, purchasing, or receiving a firearm, after examining factors the Attorney General considers are relevant to the determination, including\u2014 (aa) history of threats or acts of violence toward self or others; (bb) history of use, attempted use, or threatened use of physical force by the applicant against another person; (cc) whether the applicant is the subject of or has violated a domestic violence or stalking restraining order or protection order; (dd) any prior arrest, pending charge, or conviction for a violent or serious crime or disorderly persons offense, stalking offense, or domestic violence offense; (ee) any prior arrest, pending charge, or conviction for an offense involving cruelty to animals; (ff) history of drug or alcohol abuse or involvement in drug trafficking; (gg) any recent acquisition of firearms, ammunition, or other deadly weapons; (hh) involvement in firearms trafficking or unlawful firearms transfers; and (ii) history of unsafe storage or handling of firearms. (II) Judicial review An applicant denied a license under subclause (I) may file an action in the appropriate district court of the United States for seeking review of the denial. (C) Rule of construction Nothing in this paragraph may be construed to modify any other requirement for a background investigation relating to the acquisition or receipt of a firearm in effect on the day before the date of enactment of this section. (4) Revocation (A) In general The Attorney General shall revoke a license issued under this section if the Attorney General determines that\u2014 (i) the licensee poses a significant danger of bodily injury to self or others by possessing, purchasing, or receiving a firearm; or (ii) after a regular background investigation conducted by the Attorney General, the receipt or transfer of a firearm would violate subsection (d), (g), or (n) of section 922 or any provision of State law. (B) Notice and opportunity for a hearing (i) Notice Upon determining that the licensee should have their license revoked under subparagraph (A), the Attorney General shall provide notice to the licensee and to relevant State and local officials of the determination. (ii) Hearing For revocations under subparagraph (A)(i), the Attorney General shall provide a licensee an opportunity for a hearing in the appropriate district court of the United States not later than 30 days after the date on which a license is revoked under this paragraph to appeal the revocation. (C) Procedures The Attorney General shall establish procedures to ensure that any firearm is removed from any individual when the individual\u2019s license is revoked under this paragraph. (D) Return of firearms A firearm removed under the procedures established under subparagraph (C) may be returned to the individual only if the individual\u2019s license is reinstated. (5) Renewal The Attorney General\u2014 (A) shall establish procedures for the renewal of a license that requires that the applicant satisfies the requirements described in paragraph (2); and (B) may develop procedures and processes to consolidate renewal applications for individuals with multiple firearm purchasing licenses. (6) Enrollment in Rap Back The Attorney General shall enroll each individual who is issued a license under this section in the Rap Back service. (c) Recordkeeping It shall be unlawful for any individual to sell or otherwise dispose of a firearm to a person unless the individual reports the transaction to the Attorney General not later than 3 business days after the date on which the firearm is sold or transferred, which shall include identifying information on the firearm seller and on the firearm transferee, including the make, model, and serial number. (d) State licenses (1) In general Subsection (a) shall not apply to an individual in a State if the Attorney General determines that the State has a process for issuing a State firearm license to eligible individuals in the State with substantially similar requirements to those described in subsection (b). (e) Regulations The Attorney General may promulgate regulations that the Attorney General determines are necessary to carry out this section. .\n##### (b) Clerical amendment\nThe table of sections for such chapter is amended by adding at the end the following:\n935. License for the acquisition or receipt of firearms.\n#### 3. Point-of-sale background check\nSection 922 of title 18, United States Code, is amended by adding at the end the following:\n(aa) Point-of-Sale background checks (1) In general It shall be unlawful for any person who is not a licensed importer, licensed manufacturer, or licensed dealer to transfer a firearm to any other person who is not so licensed, unless a licensed importer, licensed manufacturer, or licensed dealer has first taken possession of the firearm for the purpose of complying with subsection (t). (2) Compliance Upon taking possession of a firearm under paragraph (1), a licensee shall comply with all requirements of this chapter as if the licensee were transferring the firearm from the inventory of the licensee to the unlicensed transferee. (3) Return If a transfer of a firearm described in paragraph (1) will not be completed for any reason after a licensee takes possession of the firearm (including because the transfer of the firearm to, or receipt of the firearm by, the transferee would violate this chapter), the return of the firearm to the transferor by the licensee shall not constitute the transfer of a firearm for purposes of this chapter. .\n#### 4. Prohibition on transfer to certain unlicensed persons\nSection 922 of title 18, United States Code, as amended by section 3 of this Act, is amended by adding at the end the following:\n(bb) Prohibition on transfer to certain unlicensed persons It shall be unlawful for any person to\u2014 (1) sell or otherwise dispose of a firearm to any person if such person does not have a license issued under section 935 or a substantially similar State law, as determined by the Attorney General, during the previous 30 days; or (2) fail to report to the relevant law enforcement agencies the sale or disposal described in paragraph (1). .",
      "versionDate": "2025-12-17",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-20T15:10:22Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3544is.xml"
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
      "title": "Federal Firearm Licensing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Firearm Licensing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to require licenses to acquire or receive firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:33:26Z"
    }
  ]
}
```
