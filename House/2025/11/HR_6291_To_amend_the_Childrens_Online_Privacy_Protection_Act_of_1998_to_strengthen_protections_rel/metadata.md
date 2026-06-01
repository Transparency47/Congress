# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6291?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6291
- Title: Children and Teens’ Online Privacy Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 6291
- Origin chamber: House
- Introduced date: 2025-11-25
- Update date: 2025-12-13T09:07:06Z
- Update date including text: 2025-12-13T09:07:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-25: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-25 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by the Yeas and Nays: 14 - 10.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-11-25: Introduced in House

## Actions

- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-25 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by the Yeas and Nays: 14 - 10.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-25",
    "latestAction": {
      "actionDate": "2025-11-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6291",
    "number": "6291",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Children and Teens\u2019 Online Privacy Protection Act",
    "type": "HR",
    "updateDate": "2025-12-13T09:07:06Z",
    "updateDateIncludingText": "2025-12-13T09:07:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by the Yeas and Nays: 14 - 10.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-25",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-25",
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
      "actionDate": "2025-11-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-25",
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
          "date": "2025-11-25T16:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-11T21:49:07Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:48:57Z",
                "name": "Markup by"
              },
              {
                "date": "2025-11-25T21:48:48Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
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
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6291ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6291\nIN THE HOUSE OF REPRESENTATIVES\nNovember 25, 2025 Mr. Walberg (for himself and Ms. Lee of Florida ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Children\u2019s Online Privacy Protection Act of 1998 to strengthen protections relating to the online collection, use, and disclosure of personal information of children and teens, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Children and Teens\u2019 Online Privacy Protection Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nSec.\u20022.\u2002Amendments to Children\u2019s Online Privacy Protection Act of 1998.\nSec.\u20023.\u2002Reports.\nSec.\u20024.\u2002Severability.\n#### 2. Amendments to Children\u2019s Online Privacy Protection Act of 1998\n##### (a) Definitions\nSection 1302 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 ) is amended\u2014\n**(1)**\nby amending paragraph (2) to read as follows:\n(2) Operator The term operator \u2014 (A) means any person\u2014 (i) who, for commercial purposes, operates or provides a website, an online service, an online application, or a mobile application; and (ii) who\u2014 (I) collects or maintains, either directly or through a service provider, personal information of users of the website, service, or application; (II) allows another person to collect personal information directly from users of the website, service, or application (in which case, the operator is deemed to have collected the information); or (III) allows users of the website, service, or application to publicly disclose personal information (in which case, the operator is deemed to have collected the information); and (B) does not include any organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code. ;\n**(2)**\nin paragraph (4)\u2014\n**(A)**\nby amending subparagraph (A) to read as follows:\n(A) the release of personal information collected from a child or teen by an operator for any purpose, except if the personal information is provided to a person other than an operator who\u2014 (i) provides support for the internal operations of the website, online service, online application, or mobile application of the operator, excluding any activity relating to individual-specific advertising provided to children or teens; and (ii) does not disclose or use the personal information for any other purpose; and ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin the matter preceding clause (i)\u2014\n**(I)**\nby inserting or teen after child each place the term appears;\n**(II)**\nby striking website or online service and inserting website, online service, online application, or mobile application ; and\n**(III)**\nby striking actual knowledge and inserting knowledge ; and\n**(ii)**\nin clause (i), by striking a website and inserting such a website, service, or application ;\n**(3)**\nby amending paragraph (8) to read as follows:\n(8) Personal information (A) In general The term personal information means individually identifiable information about an individual collected online, including\u2014 (i) a first and last name; (ii) a home or other physical address, including a street name and a name of a city or town; (iii) an e-mail address; (iv) a telephone number; (v) a Social Security number; (vi) a persistent identifier that can be used to recognize a specific child or teen over time and across different websites, online services, online applications, or mobile applications, that\u2014 (I) includes\u2014 (aa) a customer number held in a cookie; (bb) an Internet Protocol (IP) address; (cc) a processor or device serial number; and (dd) a unique device identifier; and (II) excludes an identifier that is used by an operator solely for providing support for the internal operations of a website, online service, online application, or mobile application of the operator; (vii) a photograph, video, or audio file that contains the image or voice of a child or teen; (viii) geolocation information; (ix) information generated from the measurement or technological processing of the biological, physical, or physiological characteristics of an individual, including\u2014 (I) fingerprints; (II) voice prints; (III) iris or retina imagery scans; (IV) facial templates; (V) deoxyribonucleic acid (DNA) information; and (VI) gait; (x) information linked or reasonably linkable to a child or teen or a parent of a child or teen (including any unique identifier) that an operator collects online from the child or teen and combines with an identifier described in this subparagraph; and (xi) any other identifier that the Commission determines permits the physical or online contacting of an individual. (B) Exclusion The term personal information does not include an audio file that contains the voice of a child or teen if the operator\u2014 (i) does not request information via voice that would otherwise be considered personal information under this paragraph; (ii) provides clear notice in the privacy policy of a website, online service, online application, or mobile application of the operator regarding\u2014 (I) the collection and use of such an audio file; and (II) the deletion policy relating to such an audio file; (iii) only uses the voice contained in the audio file as a replacement for written words to perform a task or otherwise engage with such website, service, or application, including by conducting a search or fulfilling a verbal instruction or request; (iv) only maintains the audio file during the period necessary to complete the relevant task or engagement; (v) does not make any other use of the audio file during such period; and (vi) deletes the audio file at the end of such period. (C) Support for the internal operations of a website, online service, online application, or mobile application (i) In general For purposes of subparagraph (A)(vi)(II), the term support for the internal operations of a website, online service, online application, or mobile application means the activities necessary to such website, service, or application to\u2014 (I) maintain or analyze functioning; (II) perform network communications; (III) authenticate users; (IV) personalize content; (V) serve contextual advertising to users (if any persistent identifier is only used as necessary for technical purposes to serve the contextual advertisement or cap the frequency of contextual advertising); (VI) protect\u2014 (aa) the integrity of the website, service, or application; or (bb) the personal information or security of users; (VII) ensure compliance with Federal or State law; and (VIII) fulfill a request of a child or teen under subparagraph (A), (B), or (C) of section 1303(b)(2). (ii) Condition Except as permitted under clause (i), information collected through the activities described in clause (i) may not be used or disclosed to contact an individual (including through individual-specific advertising provided to children or teens), to amass a profile on an individual, in connection with processes that encourage or prompt use of a website or online service, or for any other purpose. ;\n**(4)**\nby amending paragraph (9) to read as follows:\n(9) Verifiable consent The term verifiable consent means any reasonable effort (taking into consideration available technology) by an operator, including a request for authorization for future collection, use, and disclosure of personal information, to ensure that a parent of a child (in the case of a child) or a teen (in the case of a teen)\u2014 (A) receives direct notice of the collection, use, and disclosure practices of the operator with respect to personal information; and (B) before the personal information of the child or teen is collected, freely and unambiguously authorizes\u2014 (i) the collection, use, and disclosure, as applicable, of the personal information; and (ii) any subsequent use of the personal information. ;\n**(5)**\nin paragraph (10)\u2014\n**(A)**\nin the heading, by striking Website or online service directed to children and inserting Website, online service, online application, or mobile application directed to children ;\n**(B)**\nby striking website or online service directed to children each place it appears and inserting website, online service, online application, or mobile application directed to children ;\n**(C)**\nby striking commercial website or online service each place it appears and inserting website, online service, online application, or mobile application ; and\n**(D)**\nby adding at the end the following new subparagraph:\n(C) Rule of construction In considering whether a website, online service, online application, or mobile application, or a portion thereof, is directed to children, the Commission shall apply a totality of circumstances test considering competent and reliable evidence regarding the intended audience of the website, service, or application. ; and\n**(6)**\nby adding at the end the following:\n(13) Online application The term online application means an internet-connected software program. (14) Mobile application The term mobile application means a software program that runs on the operating system of\u2014 (A) a cellular telephone; (B) a tablet computer; or (C) a similar portable computing device that transmits data over a wireless connection. (15) Geolocation information The term geolocation information means information sufficient to identify a street name and name of a city or town. (16) Teen The term teen means an individual over the age of 12 and under the age of 17. (17) High-impact social media company The term high-impact social media company means a website, online service, online application, or mobile application of an operator that\u2014 (A) generates $3,000,000,000 or more in annual revenue, including any revenue generated by any affiliate of such operator; (B) has 300,000,000 or more monthly active users for not fewer than 3 of the preceding 12 months on the website, online service, online application, or mobile application of such operator; and (C) constitutes an online product or service that is primarily used by users to access or share user-generated content. (18) Knowledge The term knowledge means\u2014 (A) with respect to a high-impact social media company, the operator has actual knowledge, or willfully disregarded information that would lead a reasonable and prudent person to determine, that a user is a child or teen; and (B) with respect to an operator that does not meet the requirements of subparagraph (A), actual knowledge. (19) Individual-specific advertising to children or teens (A) In general The term individual-specific advertising to children or teens means advertising or any other effort to market a product or service that is directed to a child or teen based on\u2014 (i) personal information of\u2014 (I) the child or teen; or (II) a group of children or teens who are similar in sex, age, household income level, race, or ethnicity to the child or teen to whom the product or service is marketed; or (ii) profiling of such child or teen or group of children or teens. (B) Exclusions The term individual-specific advertising to children or teens does not include\u2014 (i) advertising or marketing to an individual or to a device of an individual in response to a request by the individual for information or feedback, such as a search query by a child or teen; (ii) contextual advertising, including if an advertisement is displayed based on the content of the website, online service, online application, or mobile application on which the advertisement appears and does not vary based on personal information of an individual who views the advertisement; (iii) processing personal information solely for measuring or reporting advertising or content performance, reach, or frequency, including through independent measurement; or (iv) advertising or marketing directed to a device used by both adult and child or teen members of a household, if such advertising or marketing is directed only to services accessible through an adult user profile. (C) Rule of construction Nothing in subparagraph (A) may be construed to prohibit an operator with knowledge that a user is a child or teen from delivering advertising or marketing that is age-appropriate and intended for a child or teen audience, if the operator does not use any personal information other than whether the user is a child or teen. (20) Educational agency or institution The term \u2018educational agency or institution\u2019 means\u2014 (A) a State educational agency or a local educational agency (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )); and (B) an elementary school or secondary school (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )). .\n##### (b) Online collection, use, disclosure, and deletion of personal information of children and teens\nSection 1303 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6502 ) is amended\u2014\n**(1)**\nby striking the heading and inserting the following: Online collection, use, disclosure, and deletion of personal information of children and teens. ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) In general It is unlawful for an operator of a website, online service, online application, or mobile application directed to children or for any operator of a website, online service, online application, or mobile application with knowledge that a user of such website, service, or application is a child or teen\u2014 (A) to collect personal information from a child or teen in a manner that violates the regulations promulgated under subsection (b); (B) to collect, use, disclose to third parties, or maintain personal information of a child or teen for the purpose of providing individual-specific advertising to children or teens (or to allow another person to collect, use, disclose, or maintain such information for such purpose); (C) to collect personal information of a child or teen, except if the collection of the personal information is\u2014 (i) consistent with the context of a particular transaction or service or the relationship of the child or teen with the operator, including any collection necessary to fulfill a transaction or provide a product or service requested by the child or teen; or (ii) authorized or required by Federal or State law; (D) to retain the personal information of a child or teen for longer than is reasonably necessary to fulfill a transaction or provide a service requested by the child or teen, except as authorized or required by Federal or State law; or (E) with respect to the personal information of a child or teen\u2014 (i) to store such information in a covered nation (as defined in section 4872(f) of title 10, United States Code), unless notice of such storage is provided to the parent of such child or to such teen, as the case may be; (ii) to transfer such information to such a nation, unless notice of such transfer is provided to the parent of such child or to such teen, as the case may be; or (iii) to provide such a nation with access to such information, unless notice of such access is provided to the parent of such child or to such teen, as the case may be. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the heading, by striking parent and inserting parent or teen ;\n**(ii)**\nby striking an operator of such a website or online service nor the operator\u2019s agent and inserting an operator of such a website, service, or application nor an agent of such an operator ; and\n**(iii)**\nby striking subsection (b)(1)(B)(iii) to the parent of a child and inserting subsection (b)(1)(B)(iv) to a parent of a child or under subsection (b)(1)(C)(iv) to a teen ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin the matter preceding clause (i), by striking the operator of any website and all that follows through from a child and inserting an operator of a website, online service, online application, or mobile application directed to children or that has knowledge that a user is a child or teen ;\n**(II)**\nin clause (i)\u2014\n**(aa)**\nby striking notice on the website and inserting clear and conspicuous notice on the website, service, or application ;\n**(bb)**\nby inserting or teens after children ;\n**(cc)**\nby striking , and the operator\u2019s disclosure practices and inserting , the disclosure practices of the operator ; and\n**(dd)**\nby striking ; and and inserting , the rights and opportunities available to a parent of a child or teen and a teen under subparagraphs (B) and (C), and the procedures or mechanisms the operator uses to ensure that personal information is not collected from children or teens (except as permitted by the regulations promulgated under this subsection); ;\n**(III)**\nin clause (ii)\u2014\n**(aa)**\nby striking parental ;\n**(bb)**\nby inserting or teens after children ; and\n**(cc)**\nby striking the semicolon at the end and inserting ; and ; and\n**(IV)**\nby inserting after clause (ii) the following new clause:\n(iii) to obtain verifiable consent from a parent of a child (in the case of a child) or from a teen (in the case of a teen) before using or disclosing personal information of the child or teen for any purpose that is a material change from how the operator uses such information or from the disclosure practices specified to the parent of the child or the teen under clause (i); ;\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin the matter preceding clause (i), by striking that website or online service and inserting the operator ;\n**(II)**\nin clause (i), by striking that operator and inserting the operator, the method by which the operator obtains the personal information, and the purposes for which the operator collects, uses, discloses, and retains the personal information before the semicolon;\n**(III)**\nin clause (ii)\u2014\n**(aa)**\nby inserting to delete personal information collected from the child or content or information submitted by the child to a website, online service, online application, or mobile application of the operator and after the opportunity at any time ; and\n**(bb)**\nby striking from that child; and and inserting of the child; ;\n**(IV)**\nby redesignating clause (iii) as clause (iv) and inserting after clause (ii) the following new clause:\n(iii) the opportunity to challenge the accuracy of the personal information and, if the parent of the child establishes the inaccuracy of the personal information, to have the inaccurate personal information corrected; and ; and\n**(V)**\nin clause (iv), as so redesignated, by striking from that child; and inserting of the child, if such information is available to the operator at the time the parent makes the request; ;\n**(iii)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (D) and (E), respectively;\n**(iv)**\nby inserting after subparagraph (B) the following new subparagraph:\n(C) require the operator, upon the request of a teen (or a parent of the teen) who has provided personal information to the operator, to provide to the teen or parent (upon authentication of the teen or parent through reasonable means)\u2014 (i) a description of the specific types of personal information collected from the teen by the operator, the method by which the operator obtains the personal information, and the purposes for which the operator collects, uses, discloses, and retains the personal information; (ii) the opportunity at any time to delete personal information collected from the teen or content or information submitted by the teen to a website, online service, online application, or mobile application of the operator; (iii) the ability to refuse to permit the operator any further use or maintenance, in retrievable form or online collection, of personal information of the teen; (iv) the opportunity to challenge the accuracy of the personal information and, if the teen or parent establishes the inaccuracy of the personal information, to have such inaccurate personal information corrected; and (v) notwithstanding any other provision of law, a means that is reasonable under the circumstances for the teen or parent to obtain any personal information collected from the teen, if such information is available to the operator at the time the teen or parent makes the request; ;\n**(v)**\nin subparagraph (D), as so redesignated\u2014\n**(I)**\nby striking a child\u2019s participation and inserting the participation of a child or teen ; and\n**(II)**\nby inserting or teen after the child ; and\n**(vi)**\nby amending subparagraph (E), as so redesignated, to read as follows:\n(E) require the operator\u2014 (i) to establish, implement, and maintain reasonable security practices to protect the confidentiality, integrity, and accessibility of personal information of children or teens collected by the operator; and (ii) to protect such personal information against unauthorized access. ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking verifiable parental consent and inserting verifiable consent ;\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nby inserting or teen after collected from a child ;\n**(II)**\nby inserting or teen after request from the child ; and\n**(III)**\nby inserting or teen or to contact another child or teen after to recontact the child ;\n**(iii)**\nin subparagraph (B)\u2014\n**(I)**\nby striking parent or child and inserting parent or teen ; and\n**(II)**\nby striking parental consent each place the term appears and inserting verifiable consent ;\n**(iv)**\nin subparagraph (C)\u2014\n**(I)**\nin the matter preceding clause (i), by inserting or teen after child each place the term appears;\n**(II)**\nin clause (i)\u2014\n**(aa)**\nby inserting or teen after child each place the term appears; and\n**(bb)**\nby inserting or teen, as applicable, after parent each place the term appears; and\n**(III)**\nin clause (ii)\u2014\n**(aa)**\nby inserting or teen, as applicable, after parent ; and\n**(bb)**\nby inserting or teen after child each place the term appears;\n**(v)**\nin subparagraph (D)\u2014\n**(I)**\nin the matter preceding clause (i)\u2014\n**(aa)**\nby inserting or teen after child each place the term appears; and\n**(bb)**\nby striking participant on the site and inserting who is a user of a website, online service, online application, or mobile application ;\n**(II)**\nin clause (ii), by inserting or teen after child ;\n**(III)**\nin clause (iii), by striking site and inserting website, service, or application ; and\n**(IV)**\nin the flush text following clause (iii)\u2014\n**(aa)**\nby inserting or teen, as applicable, after parent each place the term appears; and\n**(bb)**\nby inserting or teen after child ; and\n**(vi)**\nin subparagraph (E)\u2014\n**(I)**\nin the matter preceding clause (i), by striking website or online service and insert website, service, or application ; and\n**(II)**\nin clause (i), by striking its website and inserting the website, service, or application ;\n**(C)**\nby redesignating paragraph (3) as paragraph (4) and inserting after paragraph (2) the following new paragraph:\n(3) Application to operators acting under agreements with educational agencies or institutions The regulations promulgated under this subsection may provide that verifiable consent under paragraph (1)(A)(ii) is not required for an operator that acts under a written agreement with an educational agency or institution that requires\u2014 (A) the operator to\u2014 (i) limit the collection, use, and disclosure by the operator of the personal information of a child or teen who is a student served by the educational agency or institution to solely educational purposes and for no other commercial purposes; (ii) provide notice to the educational agency or institution regarding the specific types of personal information the operator collects from such a child or teen, the method by which the operator obtains the personal information, and the purposes for which the operator collects, uses, discloses, and retains the personal information; (iii) provide to the educational agency or institution a link regarding the disclosure practices of the operator described in subsection (b)(1)(A)(i); and (iv) upon request by the educational agency or institution\u2014 (I) provide the educational agency or institution with a means to review the personal information collected from such a child or teen; (II) prevent any further use, maintenance, or collection of personal information of such a child or teen; and (III) delete personal information collected from such a child or teen or content or information submitted by such a child or teen to the website, online service, online application, or mobile application of the operator; (B) a representative of the educational agency or institution to provide\u2014 (i) the name of the representative; (ii) the title of the representative at the educational agency or institution; and (iii) an acknowledgment that the representative has authority to permit the collection, use, and disclosure of personal information of children or teens who are students served by the educational agency or institution on behalf of the educational agency or institution; and (C) the educational agency or institution to\u2014 (i) provide on a publicly available website of the educational agency or institution a notice that\u2014 (I) identifies the operator with which the educational agency or institution has entered into a written agreement under this paragraph; and (II) includes the link described in subparagraph (A)(iii); (ii) upon request, provide the notice described in subparagraph (A)(ii) to a parent (in the case of a child who is a student served by the educational agency or institution) or a parent or teen (in the case of a teen who is a student served by the educational agency or institution); and (iii) upon the request of a parent (in the case of such a child) or a parent or teen (in the case of such a teen), request the operator provide a means to review the personal information of such child or teen and provide such parent or teen a means to review the personal information. ;\n**(D)**\nby amending paragraph (4), as so redesignated, to read as follows:\n(4) Termination of service The regulations promulgated under this subsection shall permit an operator to terminate service provided to a child for whom a parent has refused or a teen who has refused (under the regulations promulgated under paragraphs (1)(B)(ii) and (1)(C)(ii), respectively) to permit the operator any further use or maintenance, in retrievable form or online collection, of personal information of the child or teen. ; and\n**(E)**\nby adding at the end the following new paragraphs:\n(5) Continuation of service The regulations promulgated under this subsection shall prohibit an operator from discontinuing service provided to a child or teen on the basis of a request by a parent of the child or by the teen (under the regulations promulgated under paragraphs (1)(B)(ii) and (1)(C)(ii), respectively) to delete personal information collected from the child or teen, to the extent that the operator is capable of providing such service without such information. (6) Rule of construction A request to delete or correct personal information of a child or teen (under the regulations promulgated under paragraphs (1)(B) or (1)(C), respectively) may not be construed\u2014 (A) to limit the authority of a law enforcement agency to obtain any content or information from an operator pursuant to a lawfully executed warrant or an order of a court of competent jurisdiction; (B) to require an operator to delete or correct information that\u2014 (i) the operator is required to maintain under any other provision of Federal or State law; or (ii) was submitted to the website, online service, online application, or mobile application of the operator by any person other than the user who has requested that the content or information be deleted or corrected, including content or information submitted by the user that was republished or resubmitted by another person; or (C) to prohibit an operator from\u2014 (i) retaining a record of the request for deletion or correction and the information necessary to comply with a request made under the regulations promulgated under paragraphs (1)(B) or (1)(C); (ii) preventing, detecting, protecting against, or responding to security incidents, identity theft, or fraud, or reporting a person responsible for any such action; (iii) protecting the integrity or security of a website, online service, online application, or mobile application of the operator; or (iv) ensuring that the personal information of the child or teen remains deleted. (7) Common verifiable consent mechanism (A) In general (i) Feasibility of mechanism The Commission, with notice and public comment, shall assess the feasibility of allowing an operator to use a common verifiable consent mechanism that meets the requirements of this title. (ii) Requirements The feasibility assessment required by clause (i) shall consider whether a single operator could use a common verifiable consent mechanism to obtain verifiable consent from a parent of a child or from a teen on behalf of multiple, listed operators that provide a joint or related service. (B) Report Not later than 1 year after the date of the enactment of this paragraph, the Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report detailing the results of the feasibility assessment required by subparagraph (A)(i). (C) Regulations If the Commission determines in the feasibility assessment required by subparagraph (A)(i) that the use of a common verifiable consent mechanism is feasible and meets the requirements of this title, the Commission shall promulgate regulations to permit the use of such a common verifiable consent mechanism in accordance with such determination. ;\n**(4)**\nin subsection (c), by striking a regulation prescribed under subsection (a) and inserting subsection (a)(1) or a regulation promulgated under subsection (b) ; and\n**(5)**\nby amending subsection (d) to read as follows:\n(d) Preemption No State, or political subdivision of a State, may maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law that relates to the provisions of this Act. .\n##### (c) Safe harbors\nSection 1304 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6503 ) is amended\u2014\n**(1)**\nin subsection (b)(1), by inserting and teens after children ; and\n**(2)**\nby adding at the end the following:\n(d) Publication (1) In general Except as provided in paragraph (2), the Commission shall publish on the website of the Commission any report or documentation required under this title to be submitted to the Commission. (2) Restrictions on publication Notwithstanding the publication requirement described in paragraph (1), the restrictions described in sections 6(f) and 21 of the Federal Trade Commission Act ( 15 U.S.C. 46(f) ; 57b\u20132) applicable to the disclosure of information obtained by the Commission shall apply in the same manner to any publication under paragraph (1). .\n##### (d) Actions by States\nSection 1305 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6504 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by inserting section 1303(a)(1) or before any regulation ; and\n**(B)**\nin subparagraph (B), by inserting section 1303(a)(1) or before the regulation ; and\n**(2)**\nin subsection (d)\u2014\n**(A)**\nby inserting section 1303(a)(1) or before any regulation ; and\n**(B)**\nby inserting section 1303(a)(1) or before that regulation .\n##### (e) Administration and applicability of Act\nSection 1306 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6505 ) is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nby striking a rule of the Commission under section 1303 and inserting section 1303(a)(1) or a regulation promulgated under section 1303(b) ; and\n**(B)**\nby striking such rule and inserting such section or such regulation ; and\n**(2)**\nby adding at the end the following new subsection:\n(f) Additional requirement Any regulation promulgated under this title shall include a description and analysis of the impact of proposed and final rules on small entities per the Regulatory Flexibility Act of 1980 ( 5 U.S.C. 601 et seq. ). .\n#### 3. Reports\n##### (a) Oversight report\nNot later than 3 years after the date of the enactment of this Act, the Federal Trade Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report detailing the processes of high-impact social media companies to ensure that, for such companies that are websites, online services, online applications, or mobile applications directed to children, such websites, services, or applications operate in accordance with this Act, including the amendments made by this Act and the regulations promulgated under this Act.\n##### (b) Enforcement report\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter, the Federal Trade Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that details the following:\n**(1)**\nThe number of actions brought by the Commission during the reporting year to enforce the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 ) (referred to in this subsection as the Act ) and the outcome of each such action.\n**(2)**\nThe number of investigations or inquiries into potential violations of the Act during the reporting year.\n**(3)**\nThe number of open investigations or inquiries into potential violations of the Act as of the date on which the report is submitted.\n**(4)**\nThe number and nature of complaints received by the Commission relating to an allegation of a violation of the Act during the reporting year.\n#### 4. Severability\nIf any provision of this Act or the application of this Act to any person or circumstance is held invalid, the remaining provisions of this Act and the application of this Act to other persons or circumstances shall not be affected.",
      "versionDate": "2025-11-25",
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
        "name": "Commerce",
        "updateDate": "2025-12-09T22:19:04Z"
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
      "date": "2025-11-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6291ih.xml"
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
      "title": "Children and Teens\u2019 Online Privacy Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-26T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Children and Teens\u2019 Online Privacy Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Children's Online Privacy Protection Act of 1998 to strengthen protections relating to the online collection, use, and disclosure of personal information of children and teens, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-26T09:18:24Z"
    }
  ]
}
```
