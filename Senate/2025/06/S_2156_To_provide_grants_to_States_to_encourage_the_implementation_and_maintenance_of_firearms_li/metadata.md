# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2156?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2156
- Title: MASS Act
- Congress: 119
- Bill type: S
- Bill number: 2156
- Origin chamber: Senate
- Introduced date: 2025-06-24
- Update date: 2025-12-05T21:40:48Z
- Update date including text: 2025-12-05T21:40:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in Senate
- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-24: Introduced in Senate

## Actions

- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2156",
    "number": "2156",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "MASS Act",
    "type": "S",
    "updateDate": "2025-12-05T21:40:48Z",
    "updateDateIncludingText": "2025-12-05T21:40:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T21:07:21Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2156is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2156\nIN THE SENATE OF THE UNITED STATES\nJune 24, 2025 Mr. Markey (for himself and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide grants to States to encourage the implementation and maintenance of firearms licensing requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making America Safe and Secure Act of 2025 or the MASS Act .\n#### 2. Firearms licensing\n##### (a) In general\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP Firearms licensing 3061. Definitions (a) In general In this part\u2014 (1) the term covered license means a\u2014 (A) firearms license; or (B) firearms dealer license; (2) the term domestic violence protection order means a protection order, as defined in section 2266 of title 18, United States Code; (3) the term extreme risk protection order \u2014 (A) means a written order, issued by a State court or signed by a magistrate that, for a period not to exceed a time frame established by the State\u2014 (i) prohibits the individual named in the order from having under the custody or control of the individual, purchasing, possessing, or receiving a firearm or ammunition; and (ii) requires that any firearm or ammunition under the custody or control of the individual be removed; and (B) does not include a domestic violence protection order; (4) the term prohibited individual means an individual who is categorically ineligible to receive a covered license; (5) the term suitable means that an individual does not create a risk to public safety; and (6) the term thorough background check means a Federal and State background check, which may include a fingerprint-based background check. (b) Prohibited individuals For purposes of this part, a State\u2014 (1) shall establish standards for categorizing an individual as a prohibited individual for purposes of receiving a covered license; and (2) in establishing standards with respect to a covered license under paragraph (1), shall take into consideration whether limitations may be warranted based on\u2014 (A) criminal history; (B) whether an individual has been\u2014 (i) deemed a danger to himself or herself or other individuals by a court or authorized administrative body; or (ii) committed to a hospital or institution as a danger to himself or herself or other individuals; (C) age; (D) legal residency; (E) military dishonorable discharges; (F) whether an individual\u2014 (i) is subject to a permanent or temporary protection order; or (ii) has been convicted of a misdemeanor crime of domestic violence (as defined in section 921 of title 18, United States Code); (G) outstanding arrest warrants; (H) status as a fugitive; (I) renunciation of United States citizenship; and (J) other factors relevant to the suitability of a license holder. 3062. Grants and conditions (a) Grants authorized The Assistant Attorney General may make grants to States to implement or maintain firearms and firearms dealer licensing requirements. (b) Duration of grants A grant under subsection (a) shall be for a period of 3 fiscal years. (c) Use of funds for firearms and firearms dealer licensing (1) Activities Amounts received under a grant under subsection (a) shall be used for the implementation or maintenance of firearms and firearms dealer licensing requirements, which shall incorporate and implement the elements described in paragraph (2) of this subsection. (2) Elements The elements described in this paragraph are those providing that\u2014 (A) an individual shall have a firearms license\u2014 (i) at the time of the purchase, rental, or lease of a firearm or purchase of ammunition; and (ii) during the entire period of ownership or possession of a firearm or ammunition; (B) (i) an individual who (including the owner or operator of a business that) sells, rents, or leases a minimum number of firearms, or sells ammunition, during a calendar year shall obtain a firearms dealer license; and (ii) the State shall establish the minimum number of firearms for purposes of clause (i), which may not be higher than 10 per calendar year; (C) the chief of police or the board or officer having control of the police department of a local government, or a designee within the same department, shall function as the licensing authority; (D) for an application for issuance or renewal of a firearms license, the licensing authority shall\u2014 (i) conduct a thorough background check, which may include\u2014 (I) conducting an interview with the applicant; (II) requiring the submission of letters of reference stating that the applicant is of sound mind and character; and (III) any other requirements the State determines relevant; and (ii) make a determination of suitability; (E) a first-time firearms license applicant shall complete safety training; (F) for an application for issuance or renewal of a firearms dealer license, the licensing authority shall conduct an investigation into the criminal history of the applicant, which may include\u2014 (i) an interview with the applicant; (ii) a thorough background check; and (iii) any other requirements the State determines relevant; (G) the State shall establish appropriate application processes for covered licenses consistent with Federal, State, and local law; (H) the State shall establish standards and processes by which licensing authorities can revoke, suspend, or deny the issuance or renewal of a covered license; (I) the State shall ensure that a revocation, suspension, or denial cannot be based on race, color, ethnicity, religion, sex, sexual orientation, or gender identity; (J) the State shall establish judicial review processes by which any applicant for or holder of a covered license may, within a reasonable time period, petition to obtain judicial review of a revocation, suspension, or denial of the issuance or renewal of a covered license; (K) the State shall establish\u2014 (i) standards and a process under which a family member of an individual who the family member fears is a danger to himself, herself, or others may petition for an extreme risk protection order; and (ii) standards for the termination or extension of an order described in clause (i); (L) the State shall establish processes under which\u2014 (i) an individual whose covered license is revoked or suspended, or whose application for issuance or renewal of a covered license is denied, shall surrender or transfer all firearms and ammunition that are or would have been covered by the license; and (ii) an individual who is subject to an extreme risk protection order or domestic violence protection order shall surrender or transfer all firearms and ammunition in the possession of the individual; (M) the State shall establish requirements with which a firearms dealer licensee must comply, which\u2014 (i) shall include requirements relating to\u2014 (I) the location at which the licensee conducts firearm or ammunition transactions; (II) the manner in which the licensee records firearm or ammunition transactions; (III) background checks for employees of the licensee; and (IV) any other matter that the State determines appropriate; and (ii) may include requirements that a licensee\u2014 (I) maintain a permanent place of business\u2014 (aa) that is not a residence; and (bb) at which the licensee conducts all firearms or ammunition transactions; (II) submit to mandatory record and inventory inspections by a licensing authority; (III) maintain a sales record book at the permanent place of business described in subclause (I) in accordance with standards established by the State; (IV) conduct a pre-employment background check on each potential employee to determine the suitability of any potential employee who may have direct and unmonitored contact with a firearm or ammunition; and (V) take any other action that the State determines appropriate; (N) the State shall promulgate rules and regulations to ensure the prompt collection, exchange, dissemination, and distribution of information pertaining to the issuance, renewal, expiration, suspension, or revocation of a covered license; (O) the State shall establish standards that are consistent with Federal and State law\u2014 (i) governing the transfer of a firearm or ammunition; and (ii) for identifying a prohibited individual, in accordance with section 3061(b); (P) the State shall promulgate rules and regulations that require a dealer or private seller of firearms or ammunition to verify the validity of a firearms license before the sale, rental, or lease of any firearm or the sale of any ammunition; (Q) a dealer or private seller of firearms or ammunition shall report all sales, rentals, and leases of firearms, and sales of ammunition, to State authorities; (R) a dealer of firearms or ammunition shall notify the licensing authority when presented with an invalid or expired firearms license; (S) any firearms licensee whose firearm or ammunition is lost or stolen shall report the loss or theft to the licensing authority and State authorities within a reasonable time frame and in a manner established by the State; (T) an individual holding a firearms license or firearms dealer license shall renew the license on a time frame established by the State; (U) an individual may not use the firearms license of the individual to purchase a firearm or ammunition for\u2014 (i) the unlawful use of the firearm or ammunition by another individual; or (ii) the resale or other transfer of the firearm or ammunition to an unlicensed individual; and (V) (i) it shall be unlawful to store or keep a firearm in any place unless the firearm is secured in a locked container or equipped with a tamper-resistant mechanical lock or other safety device, properly engaged so as to render the firearm inoperable by any individual other than the owner or other lawfully authorized user; and (ii) for purposes of clause (i), a firearm shall not be considered to be stored or kept if carried by or under the control of the owner or other lawfully authorized user. (3) Separate ammunition dealer license permitted A State that requires a license for dealing ammunition that is separate from a license for dealing firearms shall be deemed to have satisfied the requirements under paragraph (2) relating to a firearms dealer license, as that license relates to the dealing of ammunition, if the State imposes the same requirements for an ammunition dealer license as are mandated under paragraph (2) for a firearms dealer license, as that license relates to the dealing of ammunition. (d) Application To be eligible to receive a grant under subsection (a), a State shall submit to the Assistant Attorney General an application at such time, in such manner, and containing such information as the Assistant Attorney General may require, including a description of how the State will use the grant to implement or maintain firearms and firearms dealer licensing requirements that include the elements described in subsection (c)(2). (e) Annual report Each State receiving a grant under subsection (a) shall submit to the Assistant Attorney General, for each fiscal year during which the State expends amounts received under the grant, a report, at such time and in such manner as the Assistant Attorney General may reasonably require, that contains\u2014 (1) a summary of the activities carried out using amounts made available under the grant; (2) an assessment of whether the activities are achieving the elements described in subsection (c)(2); and (3) such other information as the Assistant Attorney General may require. (f) Limitations on the allocation of funds Not more than 2 percent of the amount made available to carry out this section in any fiscal year may be used by the Assistant Attorney General for salaries and administrative expenses. (g) Reallocation of appropriations A recipient of a grant under subsection (a) shall return to the Assistant Attorney General any amounts received under the grant that are not expended for a purpose described in this section. .\n##### (b) Authorization of appropriations\nSection 1001(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10261(a) ) is amended by adding at the end the following:\n(29) There are authorized to be appropriated such sums as may be necessary to carry out part PP. .",
      "versionDate": "2025-06-24",
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
        "actionDate": "2025-06-24",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4111",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MASS Act",
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
        "updateDate": "2025-07-14T15:45:47Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2156is.xml"
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
      "title": "MASS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-04T02:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MASS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-04T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Making America Safe and Secure Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-04T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide grants to States to encourage the implementation and maintenance of firearms licensing requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-04T02:18:31Z"
    }
  ]
}
```
